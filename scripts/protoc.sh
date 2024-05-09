#!/bin/bash

protoc -I=./protos --python_out=./src --pyi_out=./src ./protos/streaming-telemetry-schema.proto 
# protoc -I=./protos --python_out=./src ./protos/streaming-telemetry-schema.proto 
# protoc -I=./protos --python_out=./src --pyi_out=./src --grpc_python_out=./src ./protos/streaming-telemetry-schema.proto 
# python -m grpc_tools.protoc -I ./protos --python3_out=./src --pyi_out=./src --grpc_python_out=./src ./protos/streaming-telemetry-schema.proto 

