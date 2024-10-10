#!/bin/bash
cd hw4

gawk -F, '$3 == 2 && $13 ~ /S/' titanic.csv

cat titanic.csv | sed 's/female/F/g; s/male/M/g'

gawk -F, 'NR > 1 && $3 == 2 && $13 ~ /S/ { age = $7; gsub(/^ *| *$/, "", age); if (age != "" ) { sum += age; count++ } } END { if (count > 0) { print "Average Age:", sum / count } else { print "No valid ages found." } }' titanic.csv

