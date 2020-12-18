#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "71" > $TMPFILE
python3 part1.py test1.txt | diff $TMPFILE -

echo "51" > $TMPFILE
python3 part1.py test2.txt | diff $TMPFILE -

echo "26" > $TMPFILE
python3 part1.py test3.txt | diff $TMPFILE -

echo "437" > $TMPFILE
python3 part1.py test4.txt | diff $TMPFILE -

echo "12240" > $TMPFILE
python3 part1.py test5.txt | diff $TMPFILE -

echo "13632" > $TMPFILE
python3 part1.py test6.txt | diff $TMPFILE -

echo "701339185745" > $TMPFILE
python3 part1.py input.txt | diff $TMPFILE -

echo "pass"
