#!/bin/bash
if [ "$#" -eq "0" ]; then
    echo "no arguments supplied"
    exit 1
fi
ARGS=""
CONT=1
for var in "$@";
do
    ARGS+="-e light$CONT=$var "
    CONT=$((CONT+1))
done
docker run $ARGS --net=host turnofflightatschedule:latest