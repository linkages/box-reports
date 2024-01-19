#!/bin/bash

lastMonth="$(date +%Y-%m --date="last month")-01"
thisMonth="$(date +%Y-%m)-01"

echo "lastMonth: ${lastMonth}"
echo "thisMonth: ${thisMonth}"

npm exec --package=@box/cli -- box events --enterprise --save --json --event-types=UPLOAD,DOWNLOAD --created-after ${lastMonth} --created-before ${thisMonth}
