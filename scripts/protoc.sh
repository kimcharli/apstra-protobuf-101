#!/bin/bash

protoc -I=./protos --python_out=./src --pyi_out=./src ./protos/streaming-telemetry-schema.proto 

