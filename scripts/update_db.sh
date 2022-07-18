#!/usr/bin/env bash

echo ":::::::Initiate update db process::::::"
date

echo "Creating temporary location for csv file.."
mkdir /app/tmp

echo "Fetch csv file from spreadsheet.."
wget --no-check-certificate -O /app/tmp/elements.csv 'https://docs.google.com/spreadsheets/d/19CtR3Wuszozzpj2hj4lmcYpMPK9_c2Y9FQQsFigggeU/export?gid=0&format=csv'

echo "Add csv contents/changes into db.."
cd /app
/usr/local/bin/poetry run python manage.py importcsv --mappings='title,description,image' --model='api.AppData' --delimiter=',' tmp/elements.csv

echo "Cleanup temporary files"
rm -rf tmp

echo "Done!"
