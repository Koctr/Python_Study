# -*- coding: utf-8 -*-
__author__ = 'K0ctr'

import os
import time

"""
递归进行多层目录创建和删除
"""
# os.makedirs(r"a\b\c\d")
# os.removedirs(r"a\b\c\d")

# os.makedirs(r"E:\a\b\c\d")
# os.removedirs(r"E:\a\b\c\d")

os.mkdir(r"a")
os.rmdir(r"a")

os.listdir(r"D:")

current_path = os.getcwd()
print(current_path)
os.chdir(r"C:\Users")
print(os.getcwd())

print(os.curdir)
print(os.pardir)

os.chdir(current_path)
# os.rename("text1", "text2")
# os.rename("text2","text1")

print(os.stat("text1"))

"""
在pycharm中自动被转换为空行，无法显示\r\n
"""
print(os.linesep)

"""
环境变量的分隔符
"""
print(os.pathsep)

print(os.environ)

os.system("dir")

print(os.path.abspath("text1"))
print(os.path.split(__file__))
print(os.path.dirname(__file__))
print(os.path.exists(r"T:"))
print(os.path.isfile(os.path.dirname(__file__)))
print(os.path.isfile("text1"))
"""
是否绝对路径
"""
print(os.path.isabs("text1"))
print(os.path.isdir("text1"))
print(os.path.join(__file__, "text1"))

"""
last read time
"""
print(time.ctime(os.path.getatime(__file__)))

"""
last modify time
"""
print(time.ctime(os.path.getmtime(__file__)))

"""
create time
"""
print(time.ctime(os.path.getctime(__file__)))
