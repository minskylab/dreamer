#!/bin/bash
docker image tag $(TAG) docker.minsky.cc/dreamer
docker push docker.minsky.cc/dreamer