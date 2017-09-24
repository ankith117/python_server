"""Server Class File"""
import socket


class Server(object):
    """comment"""

    def __init__(self, ip, port):
        """comment"""

        self.ip = ip
        self.port = port
        self.Server_socket = None
        self.connection = None
        self.client_port = None
        self.data = None

    def create_socket(self):
        """comment"""

        self.Server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (self.ip, self.port)
        self.Server_socket.bind(address)
        print("Server is set to Listen to %s on port: %s" % (str(self.ip), str(self.port)))

    def listen(self):
        """comment"""

        print('Listening and waiting for a connection')
        self.Server_socket.listen(1)
        self.connection, self.client_port = self.Server_socket.accept()

    def receive(self):
        """comment"""

        print('connection from', self.client_port)
        while True:
            self.data = self.connection.recv(16)
            print('received {!r}'.format(self.data))
            if self.data:
                print('sending data back to the client')
                self.connection.sendall(self.data)
            else:
                print('no data from', self.client_port)
                break

    def close(self):
        """comment"""

        self.connection.close()
