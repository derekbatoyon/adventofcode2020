#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

python3 part2.py -r1 test_input.txt | diff test2_round1.txt -
python3 part2.py -r2 test_input.txt | diff test2_round2.txt -
python3 part2.py -r3 test_input.txt | diff test2_round3.txt -
python3 part2.py -r4 test_input.txt | diff test2_round4.txt -
python3 part2.py -r5 test_input.txt | diff test2_round5.txt -
python3 part2.py -r6 test_input.txt | diff test2_round6.txt -

echo "26" > $TMPFILE
python3 part2.py test_input.txt | diff $TMPFILE -

echo "2117" > $TMPFILE
python3 part2.py input.txt | diff $TMPFILE -

echo "pass"
