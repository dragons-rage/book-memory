#!/bin/sh

podman build -t books .
podman run --rm -it --name books -p 8000:8000 \
  -e USER=david \
  -e PASS=golie \
  -e EMAIL="david@test.com" \
  -v ~/repos/ghub/data:/app/data \
  books
