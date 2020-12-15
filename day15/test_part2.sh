#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "24065124" > $TMPFILE
python3 part2.py "1,2,16,19,18,0" | diff $TMPFILE -

echo "pass"
