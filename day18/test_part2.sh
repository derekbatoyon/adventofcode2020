#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "231" > $TMPFILE
python3 part2.py test1.txt | diff $TMPFILE -

echo "51" > $TMPFILE
python3 part2.py test2.txt | diff $TMPFILE -

echo "46" > $TMPFILE
python3 part2.py test3.txt | diff $TMPFILE -

echo "1445" > $TMPFILE
python3 part2.py test4.txt | diff $TMPFILE -

echo "669060" > $TMPFILE
python3 part2.py test5.txt | diff $TMPFILE -

echo "23340" > $TMPFILE
python3 part2.py test6.txt | diff $TMPFILE -

echo "4208490449905" > $TMPFILE
python3 part2.py input.txt | diff $TMPFILE -

echo "pass"
