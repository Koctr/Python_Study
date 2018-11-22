# -*- encoding:utf-8 -*-
# Author: Koctr
s = "测试"
byte = bytearray(s, encoding='utf=8')
print("decode bytearray: ", byte.decode(encoding="utf-8"))
byte[1] = 100
print("alter bytearray: ", byte)
