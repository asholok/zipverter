#!/bin/sh
if [ -z "$RUN_ENV" ]; then
    echo 'Please set up RUN_ENV variable'
    exit 1
fi

if [ "$RUN_ENV" = "PROD" ]; then
    git pull
fi

docker-compose stop
docker-compose rm -f
docker-compose up -d
