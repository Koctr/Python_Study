# -*-coding:utf-8-*-
# Author: Koctr


import socket


server = socket.socket()
# 绑定地址与端口
server.bind(('localhost', 6969))
# 监听
server.listen()

# 等待
print('开始等待')
# 对方连接，对方地址
conn, addr = server.accept()
print(conn, addr)

# 不能使用server直接接听，这样就无法切换
# data = server.recv(1024)
print('接收')
data = conn.recv(1024)
print('recv: ', data)
# server.send(data, upper())
conn.send(data.upper())

server.close()
