#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "71" > $TMPFILE
python3 part1.py test1.txt | diff $TMPFILE -

echo "22000" > $TMPFILE
python3 part1.py input.txt | diff $TMPFILE -

echo "pass"
