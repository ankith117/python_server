from Client2 import Client
import sys


def main():
    c = Client(None, None)
    c.ip = sys.argv[1]
    c.port = sys.argv[2]
    c.create_socket()
    msg = b"sup"
    try:
        c.send(msg)
        c.receive()
    finally:
        c.close()

if __name__ == '__main__':

    main()
