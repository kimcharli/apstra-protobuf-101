import logging
import socket

from google.protobuf.internal.decoder import _DecodeVarint
from google.protobuf.message import DecodeError

from src import streaming_telemetry_schema_pb2 as aos



def decode_varint(data):
    """ Decode a protobuf varint to an int """
    return _DecodeVarint(data, 0)[0]

def recv_message(conn, msg_type):
    """ Receive a message, prefixed with its size, from a TCP/IP socket """
    # Receive the size of the message data
    data = b''
    while True:
        try:
            data += conn.recv(1)
            size = decode_varint(data)
            break
        except IndexError:
            pass
    # Receive the message data
    data = conn.recv(size)
    logging.warning(f"recv_message {data=}")
    if len(data) == 0:
        return data
    # Decode the message
    msg = msg_type()
    msg.ParseFromString(data)
    logging.warning(f"recv_message {msg_type=} msg=\n{msg}")
    return msg

def aos_serve():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('10.85.192.46', int(4444)))
    serversocket.listen(1)
    while True:
        connection = None
        once = True
        try:
            connection, address = serversocket.accept()
            while True:
                msg = recv_message(connection, aos.AosMessage)
        except KeyboardInterrupt:
            if connection:
                connection.close()
                logging.warning('closing by KeyboardInterrupt')
            break
        except Exception as e:
            logging.warning(f"{e=}")
            raise


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')
    aos_serve()