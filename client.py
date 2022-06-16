import os
import socket
import sys

# HOST, PORT を環境変数から取得する
# 定義されていなかったら、デフォルトの値にする
# 使い方: $ HOST=localhost PORT=50000 python3 server.py
HOST = os.environ.get("HOST") or "localhost"
PORT = int(os.environ.get("PORT") or 50000)

# ソケットでやりとりするデータのサイズ
BUFSIZE = 4096


# メイン関数
def main():
    # クライアント用ソケットを作る
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # サーバにアクセスする
    client.connect((HOST, PORT))

    # サーバに送るデータ（あなたの名前）を取得する
    # コマンドを呼び出した時の第一引数か、パソコンのユーザ名を自動で取得する
    name = sys.argv[1] if len(sys.argv) > 1 else os.environ["USER"]

    # 名前を送信する
    client.sendall(name.encode())

    # レスポンスを受け取る
    data = client.recv(BUFSIZE)

    # 受け取ったデータを画面に表示する
    print(data.decode("UTF-8"), end="")

    # ソケットを閉じる
    client.close()


# メイン処理
if __name__ == "__main__":
    main()
