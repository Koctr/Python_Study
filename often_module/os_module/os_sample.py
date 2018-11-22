# -*- coding: utf-8 -*-
__author__ = 'K0ctr'


import os


"""
递归进行多层目录创建和删除
"""
os.makedirs(r"a\b\c\d")
os.removedirs(r"a\b\c\d")

os.mkdir(r"a")
os.rmdir(r"a")

os.listdir(r"D:")

print(os.getcwd())
os.chdir(r"C:\Users")
print(os.getcwd())

print(os.curdir)
print(os.pardir)