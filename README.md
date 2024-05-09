# apstra-protobuf-101
apstra-protobuf-101

# prereguisite

## protobuf

### ubuntu

```sh
sudo apt install protobuf-compiler
```

But the version may be lower than 3.19. In such case, get one from https://github.com/protocolbuffers/protobuf/releases
```
grpclab@u22-46:~/grpc$ protoc --version
libprotoc 26.1
grpclab@u22-46:~/grpc$ 
```

### mac
```
brew install protobuf
```

## uv

```sh
curl -LsSf https://astral.sh/uv/install.sh | sudo sh
```

# setup

## clone this repo

```sh
git clone https://github.com/kimcharli/apstra-protobuf-101.git
cd apstra-protobuf-101
```

## get proto file from Apstra

Platform > Streaming > Receivers (https://10.85.192.45/#/platform/streaming/receivers)
- Download messages description
- As plain text, place it under ./protos folder
[[proto](protos/streaming-telemetry-schema.proto)]

## compile proto file
```sh
scripts/protoc.sh
```

or
```
protoc -I=./protos --python_out=./src --pyi_out=./src ./protos/streaming-telemetry-schema.proto 
```

## create venv

```sh
scripts/re-venv.sh
```

or
```sh
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

```

