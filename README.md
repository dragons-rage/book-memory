# book-memory

## Status: Draft

## Description

Designed because I accidently bought a book I started and
didn't like that I had already started listening to.

## Required Apps

Built on Python 3.13

Database (TBD)

## Installation

This is meant to run in a container, either docker or kubernetes.

## Configuration

Use .env/secrets/ect to set environment variables.

```bash
# Sould only need to be set on first execution. Any changes after
# first being set will add a new user if the username doesn't exist.
DJANGO_SUPERUSER_USERNAME='' 
DJANGO_SUPERUSER_EMAIL=''
DJANGO_SUPERUSER_PASSWORD=''
```

These are optional, but highly recommended. Defaults Listed

```
DATABASE_URL=sqlite:///app/data/db.sqlite3
CACHE_URL=someredisurl
```

## Migrating through Database

Make a full backup of the database

```bash
# This is the initial dump of the data
$ python manage.py dumpdata > datadump.json


# This section cleans the database for loading data
python manage.py shell

> > > from django.contrib.contenttypes.models import ContentType
> > > ContentType.objects.all().delete()
> > > exit()

# This will load the data into the database.
$ python manage.py loaddata datadump.json

```

## Notes

I'll add information on adding migrating database types in the wiki later. AI
did a good job with instructions and I'll just update that.

## Links

- [django-environ](https://django-environ.readthedocs.io/en/latest/index.html)
- [django-extensions](https://django-extensions.readthedocs.io/en/latest/)
