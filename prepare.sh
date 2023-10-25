#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

thisMonth=$(date +%Y-%m)
monthName=$(date +%B)
rm -f ${monthName}.csv

# get the header from the CSV file
head -n1 $1 > ${monthName}.csv

# fetch all the data for this month from the CSV
grep ${thisMonth} $1 >> ${monthName}.csv
