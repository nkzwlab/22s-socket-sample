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

    client, addr = server.accept()
    client.sendall(b"Hi, nice to meet you!\n")

    print("response sent!")

    client.close()
    server.close()

    print("connection closed.")

if __name__ == "__main__":
    main()
