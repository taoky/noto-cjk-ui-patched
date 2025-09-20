#!/bin/bash -e
set -o pipefail

COMMIT=9b0f1436e455d902de067a2501422e5dc71ad16b

mkdir -p output/

# single-thread version:
# for i in src/"$COMMIT"/NotoSansCJK-*.ttc; do
#     bname=$(basename "$i")
#     ./patch.py "$i" "output/$bname"
#     echo "$bname" done
# done

ls src/"$COMMIT"/NotoSansCJK-*.ttc | parallel '
    bname=$(basename {});
    ./patch.py {} output/$bname && echo $bname done
'
