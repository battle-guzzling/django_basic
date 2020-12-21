#!/bin/bash

docker-compose build

./start_infra.sh

docker-compose run --no-deps --rm -p 8000:8000 django_basic_core_service