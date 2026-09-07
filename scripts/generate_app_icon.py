#!/usr/bin/env python3
"""Draw a simple opaque 1024x1024 Geomoji app icon (forest + peaks)."""

from __future__ import annotations

import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "Geomoji" / "Assets.xcassets" / "AppIcon.appiconset" / "AppIcon.png"
SIZE = 1024


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def in_triangle(px: float, py: float, a: tuple[float, float], b: tuple[float, float], c: tuple[float, float]) -> bool:
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    d1 = sign((px, py), a, b)
    d2 = sign((px, py), b, c)
    d3 = sign((px, py), c, a)
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (has_neg and has_pos)


def pixel(x: int, y: int) -> bytes:
    t = y / (SIZE - 1)
    r = int(lerp(24, 46, t))
    g = int(lerp(58, 78, t))
    b = int(lerp(48, 58, t))

    peaks = [
        ((80, 780), (340, 300), (620, 780), (196, 168, 122)),
        ((360, 800), (620, 220), (920, 800), (139, 115, 82)),
        ((200, 820), (512, 380), (830, 820), (212, 180, 130)),
    ]
    for a, c, d, color in peaks:
        if in_triangle(x, y, a, c, d):
            # snow cap near the tip
            tip_y = min(a[1], c[1], d[1])
            if y < tip_y + 90:
                return bytes((236, 232, 220, 255))
            return bytes((*color, 255))

    cx, cy, rad = 820, 250, 78
    dx, dy = x - cx, y - cy
    if dx * dx + dy * dy <= rad * rad:
        if dx * dx + dy * dy <= (rad - 14) ** 2:
            return bytes((232, 220, 190, 255))
        return bytes((90, 72, 48, 255))

    return bytes((r, g, b, 255))


def write_png(path: Path, size: int) -> None:
    raw = bytearray()
    for y in range(size):
        raw.append(0)
        for x in range(size):
            raw.extend(pixel(x, y))

    def chunk(tag: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b"")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(png)


if __name__ == "__main__":
    write_png(OUT, SIZE)
    print(f"Wrote {OUT} ({OUT.stat().st_size} bytes)")
