"""This file consists of the client class, its respective methods and their implementations.
   The client is designed to send, receive data and echo the data simultaneously."""

import socket
import logging

zero = 0        # Global Variable for zero.
limit = 16      # Data limit.

logging.basicConfig(filename='client.log', level=logging.INFO)


class Client:
    """Client class defines the instances and methods required for:
    1) Creating socket
    2) Sending Data
    3) Receiving Data
    4) Closing the transmission. """

    def __init__(self, ip, port):
        """init method defines the necessary instances:
        1) ip for the ip address or localhost which is used to connect to server.
        2) Port of connection which is used to connect to the port on which the server is listening.
        3) Socket object which is used to send and receive the data through.
        4) Message which has to be sent. """

        self.ip = ip
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (self.ip, self.port)
        self.client_socket.connect(address)

    def send(self, message):
        """send method takes in the message and sends the message on the created socket."""
        message = message
        logging.info('sending %s' % message)
        self.client_socket.sendall(message)
        data_received = zero
        data_expected = len(message)
        while data_received < data_expected:
            data = self.client_socket.recv(limit)
            data_expected += len(data)
            logging.info('received {!r}'.format(data))

    def close(self):
        """close method closes the created socket resulting end of transmission."""
        logging.info('Closing Transmission!')
        self.client_socket.close()
