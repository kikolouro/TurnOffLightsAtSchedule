#!/bin/bash
if [ "$#" -eq "0" ]; then
    echo "no arguments supplied"
    exit 1
fi

for var in "$@"
do
    docker run -e light=$var --net=host turnofflightatschedule:latest
done