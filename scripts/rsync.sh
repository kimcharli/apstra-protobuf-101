#!/bin/bash

rsync -rlptzv --progress --delete --exclude=.git --exclude=.venv --exclude=__pycache__ "lab@10.85.192.46:grpc/" .

