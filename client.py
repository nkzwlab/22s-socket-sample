import os
import socket

HOST = os.environ.get("HOST") or "localhost"
PORT = int(os.environ.get("PORT") or 50000)
BUFSIZE = 4096


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((HOST, PORT))

    client.sendall(b"kino-ma")

    data = client.recv(BUFSIZE)
    print(data.decode("UTF-8"), end="")

    client.close()


if __name__ == "__main__":
    main()
