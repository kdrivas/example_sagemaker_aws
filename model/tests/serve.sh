#!/bin/sh

docker run --rm --name "my_model" \
        -p 8080:8080 \
        -v "$PWD/model:/opt/ml/model" \
        -v "$PWD/input:/opt/ml/input" $1 serve
