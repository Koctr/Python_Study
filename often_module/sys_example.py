# -*- coding:utf-8 -*-
# Author: Koctr


import sys

print(sys.argv)
print(sys.maxsize)
print(sys.path)
print(sys.platform)
print(sys.version)
sys.stdout.write("please:")
"""
去掉最后的换行符
"""
print(sys.stdin.readline()[:-1])
