import sys
from pathlib import Path
from fontTools.ttLib import TTCollection, TTFont


def process_font(font, face_idx=None):
    if "OS/2" not in font:
        idx = f"face {face_idx}" if face_idx is not None else "single font"
        print(f"{idx}: no OS/2 table, skipping")
        return

    os2 = font["OS/2"]
    hhea = font["hhea"]
    idx = f"face {face_idx}" if face_idx is not None else "single font"
    print(f"== {idx} ==")
    print("os2 version :", os2.version)
    print("os2 fsSelection:", bin(os2.fsSelection))
    print("os2 ascender:", os2.sTypoAscender)
    print("os2 descender:", os2.sTypoDescender)
    print("hhea ascent :", hhea.ascent)
    print("hhea descent:", hhea.descent)


def main():
    in_path = Path(sys.argv[1])
    suffix = in_path.suffix.lower()

    if suffix == ".ttc":
        ttc = TTCollection(str(in_path))
        for i, font in enumerate(ttc.fonts):
            process_font(font, face_idx=i)
    elif suffix in (".ttf", ".otf"):
        font = TTFont(str(in_path))
        process_font(font)
    else:
        print(f"Unsupported file type: {suffix}")


if __name__ == "__main__":
    main()
