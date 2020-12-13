#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "1068781" > $TMPFILE
python3 part2.py test.txt | diff $TMPFILE -

echo "3417" > $TMPFILE
python3 part2.py test2.txt | diff $TMPFILE -

echo "754018" > $TMPFILE
python3 part2.py test3.txt | diff $TMPFILE -

echo "779210" > $TMPFILE
python3 part2.py test4.txt | diff $TMPFILE -

echo "1261476" > $TMPFILE
python3 part2.py test5.txt | diff $TMPFILE -

echo "1202161486" > $TMPFILE
python3 part2.py test6.txt | diff $TMPFILE -

echo "1118684865113056" > $TMPFILE
python3 part2.py input.txt | diff $TMPFILE -

echo "pass"
