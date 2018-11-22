# -*-coding:utf-8-*-
# Author: Koctr


import socket
import os


server = socket.socket()
server.bind(('localhost', 6969))
# 最多4个连接
server.listen(3)

while True:
    print('等待')
    conn, addr = server.accept()
    print('开始')
    while True:
        # 客户端断开时会进入死循环，因为接收到的数据为空，因此客户端不应该输入空，Linux上不会这样
        data = ''
        try:
            data = conn.recv(1024)
        except ConnectionResetError as e:
            print(e)
        if not data:
            print("client has lost...")
            break

        # print('recv: ', data)
        # conn.send(data.upper())
        # 模拟ssh，必须转码
        res = os.popen(data.decode()).read()
        conn.send(res.encode('utf-8'))
