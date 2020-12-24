#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "92658374" > $TMPFILE
python3 part1.py --moves=10 389125467 | diff $TMPFILE -

echo "67384529" > $TMPFILE
python3 part1.py --moves=100 389125467 | diff $TMPFILE -

echo "46978532" > $TMPFILE
python3 part1.py --moves=100 215694783 | diff $TMPFILE -

echo "pass"
