#!/bin/sh

docker run --rm --name "my_model" \
            -v "$PWD/model:/opt/ml/model" \
            -v "$PWD/output:/opt/ml/output" \
            -v "$PWD/input:/opt/ml/input" $1 train
