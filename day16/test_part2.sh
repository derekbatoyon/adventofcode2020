#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "410460648673" > $TMPFILE
python3 part2.py input.txt | diff $TMPFILE -

echo "pass"
