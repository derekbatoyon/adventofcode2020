#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "436" > $TMPFILE
python3 part1.py "0,3,6" | diff $TMPFILE -

echo "1" > $TMPFILE
python3 part1.py "1,3,2" | diff $TMPFILE -

echo "10" > $TMPFILE
python3 part1.py "2,1,3" | diff $TMPFILE -

echo "27" > $TMPFILE
python3 part1.py "1,2,3" | diff $TMPFILE -

echo "78" > $TMPFILE
python3 part1.py "2,3,1" | diff $TMPFILE -

echo "438" > $TMPFILE
python3 part1.py "3,2,1" | diff $TMPFILE -

echo "1836" > $TMPFILE
python3 part1.py "3,1,2" | diff $TMPFILE -

echo "536" > $TMPFILE
python3 part1.py "1,2,16,19,18,0" | diff $TMPFILE -

echo "pass"
