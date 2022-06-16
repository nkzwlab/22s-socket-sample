import os
import socket

# HOST, PORT を環境変数から取得する
# 定義されていなかったら、デフォルトの値にする
# 使い方: $ HOST=localhost PORT=50000 python3 server.py
HOST = os.environ.get("HOST") or "localhost"
PORT = int(os.environ.get("PORT") or 50000)

# ソケットでやりとりするデータのサイズ
BUFSIZE = 4096


# メイン関数
def main():
    # サーバ用ソケットを作る
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # PORT を結びつけて、接続を待ち受ける
    server.bind(("", PORT))
    server.listen()

    print(f"listening on port {PORT}...")

    # 無限ループ
    while True:
        # クライアントからのアクセスを受け付ける
        client, addr = server.accept()
        print(f"request received from '{addr[0]}:{addr[1]}'.")

        # クライアントからの入力を受け取る
        name = client.recv(BUFSIZE)
        print(f"name: {name}")

        # 入力と組み合わせてレスポンスを送る
        client.sendall(b"Hi, nice to meet you " + name + b"!\n")
        print("response sent!")

        # 接続を切る
        client.close()
        print("connection closed.")

        print()

    # 無限ループなのでここまでこないが、一応サーバのソケットを閉じておく
    server.close()


# メイン処理
if __name__ == "__main__":
    main()
