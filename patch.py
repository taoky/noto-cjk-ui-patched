#!/usr/bin/env python3
from fontTools.ttLib import TTCollection
from pathlib import Path
import argparse

USE_TYPO_BIT = 1 << 7
ASCENT = 965
DESCENT = -285


def main(args):
    ttc = TTCollection(args.input)

    for i, font in enumerate(ttc.fonts):
        assert "OS/2" in font, f"face {i}: no OS/2 table"
        assert "hhea" in font, f"face {i}: no hhea table"
        os2 = font["OS/2"]
        hhea = font["hhea"]

        os2.fsSelection |= USE_TYPO_BIT
        if getattr(os2, "version", 0) < 4:
            os2.version = 4

        hhea.ascent = ASCENT
        hhea.descent = DESCENT
        os2.sTypoAscender = ASCENT
        os2.sTypoDescender = DESCENT

    ttc.save(args.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Build Mogo Sans CJK from Noto Sans CJK."
    )
    parser.add_argument("input", type=Path, help="Input TTC file path")
    parser.add_argument("output", type=Path, help="Output TTC file path")
    args = parser.parse_args()
    main(args)
