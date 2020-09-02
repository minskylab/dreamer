#!/bin/bash
bash apply.secrets.sh
kubectl apply -f arango.yaml
kubectl get service dreamer-arangodb-serv