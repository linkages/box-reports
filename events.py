#!/usr/bin/env python

"""Box Stats report

Usage:
  events ( <file> )

"""

from docopt import docopt
from functions import eventReport
from pprint import pprint
import csv
import os
import json

try:
    from schema import Schema, And, Or, Use, SchemaError
except ImportError:
    exit('This example requires that `schema` data-validation library'
         ' is installed: \n    pip install schema\n'
         'https://github.com/halst/schema')

arguments = docopt(__doc__)

schema = Schema({
    '<file>': Schema(os.path.exists, error=f"File does not exist: {arguments['<file>']}"),
    # '--action': Or("Download", "Uploaded", "Created", error="Invalid Action: Valid actions are: Download, Uploaded, Created")
})

try:
    arugments = schema.validate(arguments)
except SchemaError as e:
    exit(e)

filename = arguments["<file>"]

# actionFilter = arguments['--action']

usage = {}

with open(filename, 'r') as f:
    data = json.load(f)

for item in data:
    # pprint(item)
    action = item["event_type"]

    # only looking for upload and download actions
    if action not in [ "UPLOAD", "DOWNLOAD"]:
        continue

    # if the upload or download is a folder then skip
    if "folder" in item["source"]["item_type"]:
        continue

    date = item["created_at"]
    day, time = date.split("T", 1)
    time2, rest = time.split("-")
    hour, minute, second = time2.split(":")
    user = item['created_by']['name']

    size = item['additional_details']['size']
    
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

    # print(f"Event type: {item['event_type']}")
    # print(f"Date: {date} == [{day}]")
    # print(f"Created by: {user}")
    # print(f"Size: {size}")
    # print()


#     reader = csv.DictReader(f)
#     for row in reader:
#         # print(f"row: {row}")
#         action = row["Action"]
#         date = row["Date"]
#         day, hour = date.split(" ", 1)
#         user = row["User Name"]
#         size = row["Size (kB)"]

#         if actionFilter != action:
#             continue
        
# # pprint(usage)

eventReport(usage)