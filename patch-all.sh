#!/bin/bash

COMMIT=9b0f1436e455d902de067a2501422e5dc71ad16b

mkdir -p output/

for i in src/"$COMMIT"/NotoSansCJK-*.ttc; do
    bname=$(basename "$i")
    ./patch.py "$i" "output/$bname"
    echo "$bname" done
done
