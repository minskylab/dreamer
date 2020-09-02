#!/bin/bash

# use case example: IMAGE=833e112cdd80 ./registry.sh 

docker image tag $IMAGE docker.minsky.cc/dreamer
docker push docker.minsky.cc/dreamer