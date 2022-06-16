import os
import socket

HOST = os.environ.get("HOST") or "localhost"
PORT = int(os.environ.get("PORT") or 50000)
BUFSIZE = 4096


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("", PORT))
    server.listen()

    print(f"listening on port {PORT}...")

    while True:
        client, addr = server.accept()
        print(f"request received from '{addr[0]}:{addr[1]}'.")

        name = client.recv(BUFSIZE)
        print(f"name: {name}")

        client.sendall(b"Hi, nice to meet you " + name + "!\n")

        print("response sent!")
        client.close()
        print("connection closed.")
        print()

    server.close()


if __name__ == "__main__":
    main()
