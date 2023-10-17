#!/usr/bin/python

"""Box upload stats

Usage:
  uploads ( <file> )  [ --tb ]

"""

from docopt import docopt
from functions import reportGB, reportTB
import csv

arguments = docopt(__doc__)
filename = arguments["<file>"]

usage = {}

with open(filename, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if "Uploaded" in row['Action']:
            if row['User Name'] in usage:
                usage[row['User Name']] = usage[row['User Name']] + float((row['Size (kB)']))
            else:
                usage[row['User Name']] = float(row['Size (kB)'])

if arguments["--tb"] is True:
    reportTB(usage)
else:
    reportGB(usage)
