from concurrent import futures
import logging
import socket

from google.protobuf.internal.decoder import _DecodeVarint
from google.protobuf.message import DecodeError

from src import streaming_telemetry_schema_pb2 as aos



def decode_varint(data):
    """ Decode a protobuf varint to an int """
    return _DecodeVarint(data, 0)[0]

# def recv_message(conn, msg_type):
def recv_message(conn):
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
    for msg_type in [aos.Alert, aos.Event, aos.PerfMon, aos.AosMessage ]:
        try:
            msg = msg_type()
            msg.ParseFromString(data)
            logging.warning(f"recv_message {msg_type=} msg=\n{msg}")
            return msg
        except DecodeError:
            continue
        except Exception:
            raise

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
                msg = recv_message(connection)
                # msg = recv_message(connection, aos.Alert)
                # msg = recv_message(connection, aos.AosMessage)
                # msg = recv_message(connection, aos.AosSequencedMessage)  # had some issue on decoding
                # logging.warning(f"AosMessage: {msg=}")

                # # buf = connection.recv(8192).decode()  # this is wrong
                # buf = connection.recv(8192)
                # if not buf:
                #     logging.warning('no data - breaking')
                #     break
                # logging.warning(f"Got data {len(buf)=} From: {address=} {buf[:8]=} {buf[8:120]=}")
                # if once:
                #     with open('test.bin', 'wb') as f:
                #         f.write(buf)
                #         once = False

                # msg = google.protobuf.message.Message()
                # msg.ParseFromString(buf)
                # logging.warning(f"{msg=}")

                # msg = protobuf.decode(buf)
                # logging.warning(f"{msg=}")             
                # aos_msg = aos.AosMessage()
                # logging.warning(f"{aos_msg.ListFields()=} {aos_msg.IsInitialized()=}")
                # # aos_msg = aos.AosSequencedMessage()
                # aos_msg.ParseFromString(buf)
                # logging.warning(f"{aos_msg=}")
        except KeyboardInterrupt:
            if connection:
                connection.close()
                logging.warning('closing by KeyboardInterrupt')
            break
        except Exception as e:
            logging.warning(f"{e=}")
            # raise


def aos_serve2():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('10.85.192.46', int(5001)))
    serversocket.listen(1)
    while True:
        connection = None
        try:
            connection, address = serversocket.accept()
            while True:
                breakpoint()
                sz = 0
                while True:
                    import struct                   
                    vbyte, = struct.unpack('b', serversocket.recv(1))
                    sz = (vbyte << 7) + (vbyte & 0x7f)
                    if not vbyte & 0x80:
                        break
                data = []
                while sz:
                    buf = serversocket.recv(sz).decode()
                    if not buf:
                        raise ValueError("Buffer receive truncated")
                    data.append(buf)
                    sz -= len(buf)
                logging.warning(f"{sz=} {data=} {b''.join(buf)=}" )

                # buf = connection.recv(8192)
                # if not buf:
                #     logging.warning('no data - breaking')
                #     break
                # logging.warning(f"data {len(buf)=} {address=} {buf[:4]=} {buf[4:]=}")

                # aos_msg = aos.AosMessage()
                # aos_msg.ParseFromString(buf)
                # logging.warning(f"{aos_msg=}")
        except KeyboardInterrupt:
            if connection:
                connection.close()
                logging.warning('closing by KeyboardInterrupt')
            break
        except Exception as e:
            logging.warning(f"{e=}")

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S')

    # with open('main.py', 'r') as f:
    #     bbb = f.read()
    #     logging.warning(f"{type(bbb)} {bbb=}")
    aos_serve()