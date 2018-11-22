# -*- encoding:utf-8 -*-
# Author: Koctr

class F1(object):
    """封装演示
       此模块的作业一要用到
    """
    def __init__(self, n):
        self.n = n
        print("F1")


class F2(object):
    """封装演示"""
    def __init__(self, arg1):
        self.a = arg1
        print("F2")


class F3(object):
    """封装演示"""
    def __init__(self, arg2):
        self.b = arg2
        print("F3")


o1 = F1("Alex")
o2 = F2(o1)
o3 = F3(o2)

# 如何输出Alex
print(o3.b.a.n)
