#!/usr/bin/env python

from PIL import Image
import argparse

def add_margin(img, top, right, bottom, left, color=(0, 0, 0)):
    width, height = img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new("RGB", (new_width, new_height), color)
    result.paste(img.convert("RGB"), (top, left))
    return result

def main(infile_prefix, top, right, bottom, left):
    images = {
        "traces": Image.open(f"{infile_prefix}_traces.png"),
        "outline": Image.open(f"{infile_prefix}_outline.png")
    }

    width, height = images["traces"].size
    print(f"traces dimensions (px): {width}x{height}")
    for key, val in images.items():
        print(f"{key} dimensions (px): {width}x{height}")
        assert val.size == (width, height), "boards not of equal dimensions, quitting"

    for key, img in images.items():
        new_image = add_margin(img, top, right, bottom, left)
        new_image.save(f"{infile_prefix}_margin_{key}.png", "png", dpi=(1000, 1000))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("infile_prefix")
    # 40px / 1000ppi = 0.04 in, approx 1mm
    parser.add_argument("--top", default=40)
    parser.add_argument("--right", default=40)
    parser.add_argument("--bottom", default=40)
    parser.add_argument("--left", default=40)

    args = parser.parse_args()

    main(args.infile_prefix, args.top, args.right, args.bottom, args.left)
