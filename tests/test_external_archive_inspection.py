"""The optional archive inspector must skip observations and verify headers."""

import io
import random
import struct
import zlib

import pytest

from scripts.inspect_external_archives import rar5_directory


def test_optional_7z_listing_does_not_scan_observation_payload(tmp_path, monkeypatch):
    py7zr = pytest.importorskip("py7zr")
    from scripts import inspect_external_archives as inspector

    payload = random.Random(0).randbytes(1_000_000)
    path = tmp_path / "synthetic.bin"
    path.write_bytes(payload)
    archive_path = tmp_path / "synthetic.7z"
    with py7zr.SevenZipFile(archive_path, "w") as archive:
        archive.write(path, "observations.bin")
    blob = archive_path.read_bytes()

    class HeaderReader(io.BytesIO):
        size = len(blob)
        transferred = requests = 0

        def read(self, count=-1):
            assert 0 <= count < 8192, "Listing attempted a large/full-body read"
            data = super().read(count)
            self.transferred += len(data)
            self.requests += 1
            assert self.transferred < 8192, "Listing scanned synthetic observation payload"
            return data

    monkeypatch.setattr(inspector, "RemoteReader", lambda url, max_bytes: HeaderReader(blob))
    result = inspector.inspect_archive("https://example.org/synthetic.7z", "7z")
    assert result["files"] == [{"path": "observations.bin", "size_bytes": len(payload), "is_directory": False}]
    assert result["complete"] and result["bytes_transferred"] < 8192


def number(value):
    result = bytearray()
    while value > 127:
        result.append((value & 127) | 128)
        value >>= 7
    return bytes(result + bytes([value]))


def block(body):
    encoded = number(len(body)) + body
    return struct.pack("<I", zlib.crc32(encoded) & 0xffffffff) + encoded


def fixture():
    main = block(bytes([1, 0, 0]))
    name = b"EIS/SOC50.csv"
    header = block(bytes([2, 2]) + number(200000) + bytes([0]) + number(100)
                   + bytes([0, 0, 0]) + number(len(name)) + name)
    start = b"Rar!\x1a\x07\x01\x00" + main + header
    payload_start = len(start)
    return start + bytes(200000) + block(bytes([5, 0, 0])), payload_start


def test_rar_directory_inspection_skips_the_entire_packed_payload():
    data, payload_start = fixture()

    class HeaderOnly(io.BytesIO):
        size = len(data)

        def read(self, count=-1):
            pos = self.tell()
            assert pos + count <= payload_start or pos >= payload_start + 200000
            return super().read(count)

    assert rar5_directory(HeaderOnly(data)) == [
        {"path": "EIS/SOC50.csv", "size_bytes": 100, "is_directory": False}
    ]


def test_rar_directory_inspection_rejects_corrupted_header():
    data, _ = fixture()
    broken = bytearray(data)
    broken[8] ^= 1
    reader = io.BytesIO(broken)
    reader.size = len(data)
    with pytest.raises(ValueError, match="CRC"):
        rar5_directory(reader)
