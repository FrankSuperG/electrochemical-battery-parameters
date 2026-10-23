"""Inspect remote ZIP/RAR5 directory metadata without extracting observations.

Explicit, optional source-review command; never invoked by catalog/viewer/CI.
ZIP uses its central directory. RAR5 skips packed data using header sizes and
checks header CRCs, following https://www.rarlab.com/technote.htm.
Only file names/sizes and transfer statistics are saved; never archive bytes.
"""

import argparse
import io
import json
from pathlib import Path
import struct
from urllib.request import Request, urlopen
import zipfile
import zlib


class RemoteReader(io.RawIOBase):
    def __init__(self, url, max_bytes=131072):
        if not url.startswith("https://"):
            raise ValueError("HTTPS source URL required")
        self.url, self.pos = url, 0
        self.transferred, self.requests, self.max_bytes = 0, 0, max_bytes
        with urlopen(Request(url, method="HEAD"), timeout=30) as response:
            self.size = int(response.headers["Content-Length"])

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, offset, whence=0):
        if whence not in (0, 1, 2):
            raise ValueError("Unknown seek origin")
        pos = offset if whence == 0 else self.pos + offset if whence == 1 else self.size + offset
        if pos < 0:
            raise ValueError("Negative source offset")
        self.pos = pos
        return pos

    def read(self, count=-1):
        count = min(count if count >= 0 else self.size - self.pos, self.size - self.pos)
        if count <= 0:
            return b""
        if self.transferred + count > self.max_bytes:
            raise ValueError("Metadata transfer budget exceeded")
        requested = f"bytes={self.pos}-{self.pos + count - 1}"
        with urlopen(Request(self.url, headers={"Range": requested}), timeout=30) as response:
            expected = f"bytes {self.pos}-{self.pos + count - 1}/{self.size}"
            if response.status != 206 or response.headers.get("Content-Range") != expected:
                raise ValueError("Exact HTTP Range response required; full download refused")
            body = response.read(count + 1)
        if len(body) != count:
            raise ValueError("Unexpected range size")
        self.pos += count
        self.transferred += count
        self.requests += 1
        return body


def vint(data, pos):
    value = 0
    for shift in range(0, 70, 7):
        byte = data[pos]
        pos += 1
        value |= (byte & 127) << shift
        if not byte & 128:
            return value, pos
    raise ValueError("Oversized RAR integer")


def rar5_directory(reader):
    """Read only RAR5 headers, skipping compressed data areas via seek."""
    if reader.read(8) != b"Rar!\x1a\x07\x01\x00":
        raise ValueError("Non-SFX RAR5 signature required")
    offset, files = 8, []
    while offset < reader.size:
        reader.seek(offset)
        prefix = reader.read(7)
        length, start = vint(prefix, 4)
        if length > 65536:
            raise ValueError("RAR header size limit exceeded")
        reader.seek(offset + start)
        header = prefix[:start] + reader.read(length)
        if zlib.crc32(header[4:]) & 0xffffffff != struct.unpack("<I", header[:4])[0]:
            raise ValueError("RAR header CRC mismatch")
        kind, pos = vint(header, start)
        flags, pos = vint(header, pos)
        packed = 0
        if flags & 1:
            _, pos = vint(header, pos)
        if flags & 2:
            packed, pos = vint(header, pos)
        if flags & 0x18:
            raise ValueError("Split archive members are not inspected")
        if kind == 4:
            raise ValueError("Encrypted archive headers are not inspected")
        if kind == 1:
            archive_flags, _ = vint(header, pos)
            if archive_flags & 1:
                raise ValueError("Multi-volume archives are not inspected")
        if kind == 2:
            file_flags, pos = vint(header, pos)
            unpacked, pos = vint(header, pos)
            _, pos = vint(header, pos)
            pos += (4 if file_flags & 2 else 0) + (4 if file_flags & 4 else 0)
            _, pos = vint(header, pos)
            _, pos = vint(header, pos)
            name_length, pos = vint(header, pos)
            name = header[pos:pos + name_length]
            if len(name) != name_length:
                raise ValueError("Truncated RAR member name")
            files.append({"path": name.decode("utf-8"),
                          "size_bytes": None if file_flags & 8 else unpacked,
                          "is_directory": bool(file_flags & 1)})
        offset += start + length + packed
        if offset > reader.size or len(files) > 10000:
            raise ValueError("Invalid archive bounds or entry limit")
        if kind == 5:
            return files
    raise ValueError("Missing RAR end header; incomplete directory")


def inspect_archive(url, kind, max_bytes=131072):
    reader = RemoteReader(url, max_bytes=max_bytes)
    if kind == "zip":
        with zipfile.ZipFile(reader) as archive:
            files = [{"path": item.filename, "size_bytes": item.file_size,
                      "is_directory": item.is_dir()} for item in archive.infolist()]
    else:
        files = rar5_directory(reader)
    return {"source_url": url, "method": f"HTTP Range {kind} directory only; no member extraction",
            "archive_size_bytes": reader.size, "bytes_transferred": reader.transferred,
            "requests": reader.requests, "complete": True, "files": files}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--kind", choices=["zip", "rar5"], required=True)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--max-bytes", type=int, default=131072)
    args = parser.parse_args()
    result = inspect_archive(args.url, args.kind, args.max_bytes)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(f"{len(result['files'])} directory entries; {result['bytes_transferred']} metadata bytes read")
