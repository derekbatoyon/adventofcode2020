#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "20899048083289" > $TMPFILE
python3 part1.py test.txt | diff $TMPFILE -

echo "22878471088273" > $TMPFILE
python3 part1.py input.txt | diff $TMPFILE -

echo "pass"
