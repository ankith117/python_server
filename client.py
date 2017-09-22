import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_port = ('localhost', 9292)
print('Transmitting to {} on port: {}'.format(*server_port))
s.connect(server_port)

try:
    message = b"Sup?"
    print('sending {!r}'.format(message))
    s.sendall(message)
    data_received = 0
    data_expected = len(message)
    while data_received < data_expected:
        data = s.recv(16)
        data_expected += len(data)
        print('received {!r}'.format(data))
finally:
    print('Closing Transmission!')
    s.close()
