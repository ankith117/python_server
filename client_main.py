from Client2 import Client
import sys


def main():

    ip = sys.argv[1]
    port = sys.argv[2]
    c = Client(ip, port)
    msg = b"sup"
    try:
        c.send(msg)
    finally:
        c.close()

if __name__ == '__main__':

    main()
