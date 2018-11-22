# -*-coding:utf-8-*-
# Author: Koctr


import socket

# 声明socket类型，同时生成socket连接对象
client = socket.socket()
client.connect(('localhost', 6969))

# client.send(b'Hello World!')
# 发送中文
client.send('中文'.encode('utf-8'))

data = client.recv(1024)
# print('recv: ', data)
# 接收中文
print('recv: ', data.decode())
client.close()
