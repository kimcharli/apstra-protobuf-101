#!/bin/bash

python -m grpc_tools.protoc -I ./protos --python_out=./src --pyi_out=./src --grpc_python_out=./src ./protos/streaming-telemetry-schema.proto 

