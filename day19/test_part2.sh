#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "12" > $TMPFILE
python3 part2.py test2.txt | diff $TMPFILE -

echo "392" > $TMPFILE
python3 part2.py input.txt | diff $TMPFILE -

echo "pass"
