from concurrent import futures
import logging
import socket

import grpc
from src import streaming_telemetry_schema_pb2
from src import streaming_telemetry_schema_pb2_grpc




def serve():

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Set SO_REUSEADDR option 
    serversocket.bind(('10.85.192.46', int(5001)))
    serversocket.listen(1)
    # server_socket.settimeout(1)  # Set timeout to handle KeyboardInterrupt gracefully

    # port = "50001"
    # server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # streaming_telemetry_schema_pb2_grpc.

    # server.add_insecure_port("[::]:" + port)
    # server.start()
    # print("Server started, listening on " + port)
    # server.wait_for_termination()

    # channel = grpc.insecure_channel('10.85.192.46:50001')
    # stub = GerrterStub(channel)
    # response = stub.SayHello(Hello)

    while True:
        connection, address = serversocket.accept()
        while True:
            buf = connection.recv(8192)
            if not buf:
                logging.warning('no data - breaking')
                break
            logging.warning(f"data {len(buf)=} {buf[:40]=}")



if __name__ == '__main__':
    logging.basicConfig()
    serve()