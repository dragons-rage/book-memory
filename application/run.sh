#!/bin/sh

python manage.py migrate || exit 1
python manage.py runscript create_user --script-args $USER "$EMAIL" $PASS
python manage.py runserver 0.0.0.0:8000 || exit 1
