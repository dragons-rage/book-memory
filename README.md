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
BOOKMEMORY_DB_SERVER=${BOOKMEMORY_DB_SERVER:-""} # empty string sqlite3
BOOKMEMORY_DB_USERNAME=${BOOKMEMORY_DB_USERNAME:-"bookkeeper"}
BOOKMEMORY_DB_PASSWORD=${BOOKMEMORY_DB_PASSWORD:-"placeholder"}
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
