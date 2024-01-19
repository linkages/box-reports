#!/bin/bash

thisMonth="$(date +%Y-%m)-01"

npm exec --package=@box/cli -- box events --enterprise --save --json --event-types=UPLOAD,DOWNLOAD --created-after ${thisMonth}
