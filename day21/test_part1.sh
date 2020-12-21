#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "5" > $TMPFILE
python3 part1.py test.txt | diff $TMPFILE -

echo "2061" > $TMPFILE
python3 part1.py input.txt | diff $TMPFILE -

echo "pass"
