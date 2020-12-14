#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "165" > $TMPFILE
python3 part1.py test.txt | diff $TMPFILE -

echo "5055782549997" > $TMPFILE
python3 part1.py input.txt | diff $TMPFILE -

echo "pass"
