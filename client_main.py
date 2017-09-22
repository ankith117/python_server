from Client2 import Client

if __name__ == '__main__':

    c = Client('localhost', 9292)
    c.create_socket()
    msg = b"sup"
    try:
        c.send(msg)
        c.receive()
    finally:
        c.close()
