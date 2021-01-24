#!/bin/sh

set -e

python -m site
cd /home/app/.local/lib/python3.6/site-packages
zip -r -X "/mnt/dist/site-packages.zip" *
