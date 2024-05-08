#!/bin/bash

rsync -rlptzv --progress --delete --exclude=.git --exclude=.venv "lab@10.85.192.46:grpc/" .

