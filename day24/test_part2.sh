#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "2208" > $TMPFILE
python3 part2.py test.txt | diff $TMPFILE -

echo "3794" > $TMPFILE
python3 part2.py input.txt | diff $TMPFILE -

echo "pass"
