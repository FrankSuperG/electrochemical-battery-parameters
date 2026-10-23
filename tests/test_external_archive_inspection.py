"""The optional archive inspector must skip observations and verify headers."""

import io
import struct
import zlib

import pytest

from scripts.inspect_external_archives import rar5_directory


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
