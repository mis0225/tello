## Tello Basics ##

### How to start programming with python ###

- TelloのSDK(Software Development Kit)を深く理解していなくても、UDPのソケットプログラムさえできれば動かすことが可能。
  - **UDP(User Datagram Protocol)**  とは、ネット上で標準的に利用されている通信プロトコル（通信規格）の一種。
    - データを送信する側が相手のコンピュータの状態にかかわらず一方的にデータを送り始める
    - データ欠損があっても問題がなく、リアルタイムにデータを送り続ける必要がある場面で利用される
  - **UDPヘッダ**とは、届けられたIPパケットの基本情報が付与されたもの。
    - IPネットワーク上で通信を行う際、データは「IPパケット」と呼ばれる小さなデータに分割して送られる
    - UDPヘッダには、「送信元ポート」「宛先ポート」「データ長」「チェックサム」の４つのデータが含まれている

以下のプログラムで動かすことが可能
```python
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDPソケットの作成
msg = input("command? = ") # 送信するコマンドをキーボード入力(command, takeoffなど)
sock.sendto(msg.encode('utf-8'), ('192.168.10.1', 8889)) # Telloへ送信

```
