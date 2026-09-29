#!/usr/bin/env python3
"""Generate placeholder PNG assets for EmptyFlowMVP.
Run from project root: python3 tools/generate_placeholder_assets.py
"""
from PIL import Image, ImageDraw
import random
import os

random.seed(42)

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def make_character_color(path):
    img = Image.new("RGBA", (2000, 2000), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle([700, 800, 1300, 1700], radius=80, fill=(70, 100, 160, 255))
    draw.ellipse([750, 400, 1250, 900], fill=(220, 180, 150, 255))
    draw.rounded_rectangle([550, 850, 720, 1400], radius=50, fill=(70, 100, 160, 255))
    draw.rounded_rectangle([1280, 850, 1450, 1400], radius=50, fill=(70, 100, 160, 255))
    draw.rounded_rectangle([750, 1650, 950, 1950], radius=50, fill=(50, 60, 90, 255))
    draw.rounded_rectangle([1050, 1650, 1250, 1950], radius=50, fill=(50, 60, 90, 255))
    ensure_dir(path)
    img.save(path)
    print(f"Generated: {path}")

def make_character_line(path):
    img = Image.new("RGBA", (2000, 2000), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    lw = 12
    draw.ellipse([750, 400, 1250, 900], outline=(0, 0, 0, 255), width=lw)
    draw.rounded_rectangle([700, 800, 1300, 1700], radius=80, outline=(0, 0, 0, 255), width=lw)
    draw.rounded_rectangle([550, 850, 720, 1400], radius=50, outline=(0, 0, 0, 255), width=lw)
    draw.rounded_rectangle([1280, 850, 1450, 1400], radius=50, outline=(0, 0, 0, 255), width=lw)
    draw.rounded_rectangle([750, 1650, 950, 1950], radius=50, outline=(0, 0, 0, 255), width=lw)
    draw.rounded_rectangle([1050, 1650, 1250, 1950], radius=50, outline=(0, 0, 0, 255), width=lw)
    draw.ellipse([880, 600, 930, 650], fill=(0, 0, 0, 255))
    draw.ellipse([1070, 600, 1120, 650], fill=(0, 0, 0, 255))
    ensure_dir(path)
    img.save(path)
    print(f"Generated: {path}")

def make_oil_bg(path, c1, c2, c3):
    width, height = 4000, 2250
    img = Image.new("RGB", (width, height), c1)
    draw = ImageDraw.Draw(img)
    for y in range(height):
        r = int(c1[0] + (c2[0] - c1[0]) * y / height)
        g = int(c1[1] + (c2[1] - c1[1]) * y / height)
        b = int(c1[2] + (c2[2] - c1[2]) * y / height)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    for _ in range(300):
        x = random.randint(0, width)
        y = random.randint(0, height)
        rx = random.randint(50, 400)
        ry = random.randint(30, 200)
        ac = (
            random.randint(min(c1[0], c3[0]), max(c1[0], c3[0])),
            random.randint(min(c1[1], c3[1]), max(c1[1], c3[1])),
            random.randint(min(c1[2], c3[2]), max(c1[2], c3[2]))
        )
        draw.ellipse([x - rx, y - ry, x + rx, y + ry], fill=ac)
    pixels = img.load()
    for _ in range(50000):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        r, g, b = pixels[x, y]
        noise = random.randint(-15, 15)
        pixels[x, y] = (max(0, min(255, r + noise)), max(0, min(255, g + noise)), max(0, min(255, b + noise)))
    ensure_dir(path)
    img.save(path)
    print(f"Generated: {path}")

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base)
    make_character_color("assets/characters/player_color.png")
    make_character_line("assets/characters/player_line.png")
    make_oil_bg("assets/worlds/world_a.png", (180, 160, 130), (220, 190, 150), (140, 110, 80))
    make_oil_bg("assets/worlds/world_b.png", (80, 100, 140), (120, 140, 180), (50, 60, 100))
    print("All placeholder assets generated.")
