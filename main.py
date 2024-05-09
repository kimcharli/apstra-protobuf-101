import logging
import socket
from enum import Enum

from google.protobuf.internal.decoder import _DecodeVarint
from google.protobuf.message import DecodeError

from src import streaming_telemetry_schema_pb2 as aos


class StreamType(Enum):
    ALERT = 'alert'
    EVENT = 'event'
    PERF_MON = 'perf_mon'

    @classmethod
    def aslist(cls):
        return [x.value for x in [cls.ALERT, cls.EVENT, cls.PERF_MON]]


def decode_varint(data):
    """ Decode a protobuf varint to an int """
    return _DecodeVarint(data, 0)[0]


def recv_message(conn, msg_type, stream_type: StreamType):
    """ Receive a message, prefixed with its size, from a TCP/IP socket """
    banner = f"recv_message({stream_type})"
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
    logging.debug(f"{banner} recv {size=}")
    if len(data) == 0:
        return data
    # Decode the message
    msg = msg_type()
    msg.ParseFromString(data)
    # logging.debug(f"recv_message() {stream_type=} {msg=}")
    match stream_type:
        case StreamType.ALERT.value:
            logging.debug(f"{banner} {msg.alert.id} {msg.origin_hostname}-{msg.origin_name}")
        case StreamType.EVENT.value:
            logging.debug(f"{banner} {msg.event.id} {msg.origin_hostname}-{msg.origin_name}")
        case StreamType.PERF_MON.value:
            # logging.debug(f"recv_message() {stream_type=} ")
            this_pf = msg.perf_mon
            for pf_item in ['interface_counters', 'system_resource_counters', 'generic', 'probe_message', 'time_delta']:
                this_pf = getattr(msg.perf_mon, pf_item)
                if this_pf:
                    match pf_item:
                        case 'interface_counters':
                            if hasattr(this_pf, 'tx_bytes'):
                                logging.debug(f"{banner} {pf_item}:{msg.origin_name}:{this_pf.tx_bytes}")
                                break
                        # case 'system_resource_counters':
                        #     pass
                        # case 'generic':
                        #     pass
                        # case 'probe_message':
                        #     pass
                        # case 'time_delta':
                        #     pass
                        case _:
                            logging.debug(f"{banner} {pf_item}:{msg.origin_name}:{this_pf}")
    return msg

def aos_serve(local_host: str, local_port: int, stream_type: StreamType):
    logging.info(f"aos_server {local_host=} {local_port=}")
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serversocket.bind((local_host, int(local_port)))
        serversocket.listen(1)  # to get Alert, Event, and Perfmon
    except OSError as e:
        logging.error(f"{e=}")
        return
    while True:
        # connection = None
        try:
            connection, address = serversocket.accept()
            logging.info(f"aos_serve connection from {address}")
            while True:
                msg = recv_message(connection, aos.AosMessage, stream_type)
        except KeyboardInterrupt:
            if connection:
                serversocket.close()
                logging.warning('closing by KeyboardInterrupt')                
            break
        except Exception as e:
            logging.warning(f"{e=}")
            raise


if __name__ == '__main__':
    """
    usage: python main.py 10.85.192.46 4446 event
    """
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')
    import sys
    logging.debug(f"{sys.argv=}")
    self_host = len(sys.argv) >= 2 and sys.argv[1] or '10.85.192.46'
    self_port = sys.argv[2] if len(sys.argv) >= 2 else 4444
    stream_type = sys.argv[3] if len(sys.argv) >= 3 else StreamType.ALERT.value
    if stream_type in StreamType.aslist():
        aos_serve(self_host, self_port, stream_type)
    else:
        logging.error(f"stream type should be one of {StreamType.aslist()}")
        sys.exit(1)
