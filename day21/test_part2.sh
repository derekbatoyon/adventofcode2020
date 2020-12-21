#!/bin/bash -e

TMPFILE=$(mktemp)
trap "rm -f $TMPFILE" EXIT

echo "mxmxvkd,sqjhc,fvjkl" > $TMPFILE
python3 part2.py test.txt | diff $TMPFILE -

echo "cdqvp,dglm,zhqjs,rbpg,xvtrfz,tgmzqjz,mfqgx,rffqhl" > $TMPFILE
python3 part2.py input.txt | diff $TMPFILE -

echo "pass"
