#!/bin/bash

# TODO get working with a production wsgi server
# /usr/local/bin/uvicorn tzfinderapp.main:app \
#   --no-access-log \
#   --host 0.0.0.0 \
#   --port 8080

python3 tzfinderapp/main.py