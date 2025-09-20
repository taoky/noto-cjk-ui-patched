#!/bin/bash -e
set -o pipefail

COMMIT=9b0f1436e455d902de067a2501422e5dc71ad16b

mkdir -p "src/$COMMIT"

# download file if not exists...
function download() {
    local url=$1
    local output=$2

    if [ ! -f "$output" ]; then
        echo "Downloading $url to $output"
        curl -L "$url" -o "$output"
    else
        echo "File $output already exists, skipping download."
    fi
}

# OTC
for name in Black Bold DemiLight Light Medium Regular Thin; do
    download "https://github.com/notofonts/noto-cjk/raw/$COMMIT/Sans/OTC/NotoSansCJK-$name.ttc" "src/$COMMIT/NotoSansCJK-$name.ttc"
done
