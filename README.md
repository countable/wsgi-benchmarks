WSGI Benchmarks
===============

Compare performance of various ways of running a flask-like app.

# Setup

You'll need to install Docker and Docker Compose if you haven't.

- Install Docker: https://docs.docker.com/engine/installation/
- Install Docker Compose: https://docs.docker.com/compose/install/

#### Build

    $ docker-compose build

#### Run

Bring up web server containers.

    $ docker-compose up -d

To run benchmarks

    $ docker-compose up ab

