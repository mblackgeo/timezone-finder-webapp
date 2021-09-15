# timezone-finder-webapp
A web front end to find the timezone by clicking on a point on map

Build on:

* [Dash-leaflet](https://dash-leaflet.herokuapp.com)
* [timezonefinder](https://github.com/jannikmi/timezonefinder)
* `python>=3.7`

## Quick Guide

To get started quickly simply clone the repository and build and run:

```shell
./build.sh && ./run-local.sh
```

This will start a local instance which can be opened in the browser at [http://0.0.0.0:8080](http://0.0.0.0:8080)

## Development

To develop, set up a new clean virtual environment and install the requirements:

```mkvirtualenv
mkvirtualenv --python=/usr/bin/python3.7 tzapp
pip3 install -r requirements.txt
pip3 install -r requirements-dev.txt
```

## TODO

Refactor to remove Dash dependency and wrap [Leaflet](https://leafletjs.com/) directly.