# -*-coding:utf-8-*-
# Author: Koctr


import socket


client = socket.socket()
client.connect(('localhost', 6969))

while True:
    msg = input('>>:')
    # 发送空，服务器端无法接收
    if len(msg) == 0:
        continue
    if msg == "exit":
        break

    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print(data.decode())

client.close()
