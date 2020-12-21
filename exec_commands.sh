#!/bin/bash

docker exec $(docker ps | grep django_basic_core_service | cut -d' ' -f1) $1 $2 $3 $4 $5