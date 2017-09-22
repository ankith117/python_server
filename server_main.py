from server import Server

if __name__ == '__main__':

    s = Server('localhost', 9292)
    s.create_socket()
    s.listen()
    while True:
        try:
            s.receive()
        finally:
            s.close()
