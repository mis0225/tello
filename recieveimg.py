"""
映像の受信、コマンドを入力するとそれに従うようになる
有効化→離陸→30cm上昇→20cm上昇→40cm下降→着陸であれば、
command
takeoff
up 30
up 20
down 40
land
(参考資料: https://algorithm.joho.info/programming/python/tello-python-command/ )
"""


import socket
import threading
import cv2
import time
import numpy as np


# recieving data
def udp_reciever():
    while True:
        try:
            response, _ = sock.recvfrom(1024)
        except Exception as e:
            print(e)
            break

# Tello address
TELLO_IP = '192.168.10.1'
TELLO_PORT = 8889
TELLO_ADDRESS = (TELLO_IP, TELLO_PORT)
TELLO_CAMERA_ADDRESS = 'udp://@0.0.0:11111' # recieving camera data

# UDP通信ソケットの作成
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 自ホストで使用するipアドレスとポート番号を設定
sock.bind('', TELLO_PORT)

# 受信用スレッドの作成
thread = threading.Thread(target=udp_reciever)
thread.daemon = True
thread.start()

while True:
    try:
        msg = input("")

        if not msg: # nothing unless any input message
            break
        
        if 'q' in msg: # quit for pressing `q`
            print('QUIT...')
            sock.close()
            break

        # データを送信
        msg = msg.encode(encoding="utf-8")
        sent = sock.sendto(msg, TELLO_ADDRESS)

    except KeyboardInterrupt:
        sock.close()
        break






