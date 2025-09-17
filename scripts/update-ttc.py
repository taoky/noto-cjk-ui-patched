import sys
from pathlib import Path
from fontTools.ttLib import TTCollection

in_path = Path(sys.argv[1])
out_path = (
    Path(sys.argv[2])
    if len(sys.argv) > 2
    else in_path.with_name(in_path.stem + "_utypo" + in_path.suffix)
)

ttc = TTCollection(str(in_path))
USE_TYPO_BIT = 1 << 7  # fsSelection bit 7

for i, font in enumerate(ttc.fonts):
    if "OS/2" not in font:
        print(f"face {i}: no OS/2 table, skipping")
        continue
    os2 = font["OS/2"]
    hhea = font["hhea"]
    before = os2.fsSelection
    os2.fsSelection = before | USE_TYPO_BIT

    # Optional: ensure OS/2 version >= 4 (where the bit is defined)
    if getattr(os2, "version", 0) < 4:
        os2.version = 4
    hhea.ascent = 965
    hhea.descent = -285
    os2.sTypoAscender = 965
    os2.sTypoDescender = -285

    print(f"face {i}: fsSelection {before:#06x} -> {os2.fsSelection:#06x}")

ttc.save(str(out_path))
print("Saved:", out_path)
