#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "848" > $TMPFILE
python3 part2.py test.txt | diff $TMPFILE -

echo "2236" > $TMPFILE
python3 part2.py input.txt | diff $TMPFILE -

echo "pass"
