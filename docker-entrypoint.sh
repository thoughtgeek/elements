#!/bin/bash

echo "Wait for db to boot"
sleep 10

echo "Apply database migrations.."
poetry run python manage.py migrate

echo "Fetch CSV and update db"
bash scripts/update_db.sh

echo "Start cronjob"
cron

echo "Running server"
poetry run uwsgi --http :${PORT} --processes ${WORKERS} --static-map /static=/static --module elements.wsgi:application
