#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "149245887792" > $TMPFILE
python3 part2.py --moves=10000000 --max=1000000 389125467 | diff $TMPFILE -

echo "163035127721" > $TMPFILE
python3 part2.py --moves=10000000 --max=1000000 215694783 | diff $TMPFILE -

echo "pass"
