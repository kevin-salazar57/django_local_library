#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install --upgrade pip
pip install psycopg2
pip install dj-database-url
pip3 install -r requirements.txt
#poetry install

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser
