# -*- encoding:utf-8 -*-
# Author: Koctr


import os


# 乱码，能解决吗？
os.system("dir")

cmd = os.system("dir")
# 结果与状态码，0为成功
print(cmd)

# 对象
cmd_res = os.popen("dir")
print(cmd_res.read())

# os.mkdir("mkdir")
