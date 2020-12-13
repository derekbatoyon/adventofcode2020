#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "295" > $TMPFILE
python3 part1.py test.txt | diff $TMPFILE -

echo "4782" > $TMPFILE
python3 part1.py input.txt | diff $TMPFILE -

echo "pass"
