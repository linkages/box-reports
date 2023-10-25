#!/usr/bin/env python

"""Box Stats report

Usage:
  report ( <file> ) ( --action=<action> )

"""

from docopt import docopt
from functions import report
from pprint import pprint
import csv
import os

try:
    from schema import Schema, And, Or, Use, SchemaError
except ImportError:
    exit('This example requires that `schema` data-validation library'
         ' is installed: \n    pip install schema\n'
         'https://github.com/halst/schema')

arguments = docopt(__doc__)

schema = Schema({
    '<file>': Schema(os.path.exists, error=f"File does not exist: {arguments['<file>']}"),
    '--action': Or("Download", "Uploaded", "Created", error="Invalid Action: Valid actions are: Download, Uploaded, Created")
})

try:
    arugments = schema.validate(arguments)
except SchemaError as e:
    exit(e)

filename = arguments["<file>"]

actionFilter = arguments['--action']

usage = {}

with open(filename, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # print(f"row: {row}")
        action = row["Action"]
        date = row["Date"]
        day, hour = date.split(" ", 1)
        user = row["User Name"]
        size = row["Size (kB)"]

        if actionFilter != action:
            continue

        if size == "":
            size = float(0)
        else:
            size = float(size)

        if action not in usage:
            usage[action] = {}
        
        if user not in usage[action]:
            usage[action][user] = {}

        if day not in usage[action][user]:
            usage[action][user][day] = size
        else:
            usage[action][user][day] = usage[action][user][day] + size
        
# pprint(usage)

report(usage)