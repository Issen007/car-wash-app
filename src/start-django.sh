#!/bin/bash
status=0
while [ $status -le 1 ]
do
  echo "Waiting for Database to start..."
  curl --no-progress-meter db:5432 > /dev/null
    if [[ "$?" -eq 52 ]]; then
        echo "Database is now up, let's continue..."
        ((status++))
    else
      sleep 10
    fi
done;

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate
gunicorn webserver.wsgi --workers=2 --threads=4 --worker-class=gthread