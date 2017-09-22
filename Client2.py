"""Client Class File"""

import socket


class Client:
    """comment"""

    def __init__(self, ip, port):
        """comment"""
        self.ip = ip
        self.port = port
        self.Client_Socket = None
        self.message = None
        self.data_received = None
        self.data_expected = None
        self.data = None

    def create_socket(self):
        """comment"""
        self.Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (self.ip, self.port)
        self.Client_Socket.connect(address)

    def send(self, message):
        """comment"""
        self.message = message
        print('sending %s' % self.message)
        self.Client_Socket.sendall(message)

    def receive(self):
        """comment"""
        self.data_received = 0
        self.data_expected = len(self.message)
        while self.data_received < self.data_expected:
            self.data = self.Client_Socket.recv(16)
            self.data_expected += len(self.data)
            print('received {!r}'.format(self.data))

    def close(self):
        """comment"""
        print('Closing Transmission!')
        self.Client_Socket.close()


