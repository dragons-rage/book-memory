#!/bin/sh
export DJANGO_SUPERUSER_USERNAME=${USER}
export DJANGO_SUPERUSER_EMAIL=${EMAIL}
export DJANGO_SUPERUSER_PASSWORD=${PASS}
python manage.py migrate || exit 1
#python manage.py runscript create_user --script-args $USER "$EMAIL" $PASS
python manage.py createsuperuser --noinput
python manage.py runserver 0.0.0.0:8000 || exit 1
