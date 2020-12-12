#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

python3 part1.py -r1 test_input.txt | diff test1_round1.txt -
python3 part1.py -r2 test_input.txt | diff test1_round2.txt -
python3 part1.py -r3 test_input.txt | diff test1_round3.txt -
python3 part1.py -r4 test_input.txt | diff test1_round4.txt -
python3 part1.py -r5 test_input.txt | diff test1_round5.txt -

echo "37" > $TMPFILE
python3 part1.py test_input.txt | diff $TMPFILE -

echo "2319" > $TMPFILE
python3 part1.py input.txt | diff $TMPFILE -

echo "pass"
