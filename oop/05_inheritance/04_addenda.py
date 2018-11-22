# -*- encoding:utf-8 -*-
# Author: Koctr


class F1(object):
    """继承过程演示"""
    def __init__(self):
        print("F1")

    def a1(self):
        print("F1a1")

    def a2(self):
        print("F1a2")


class F2(F1):
    """继承过程演示"""
    def __init__(self):
        print("F2")

    def a1(self):
        self.a2()
        print("F2a1")

    def a2(self):
        print("F2a2")


class F3(F2):
    """继承过程演示"""
    def __init__(self):
        print("F3")

    def a2(self):
        print("F3a2")

obj = F3()
obj.a1()
