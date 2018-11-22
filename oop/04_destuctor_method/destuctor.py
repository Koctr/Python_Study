# -*- coding:utf-8 -*-
# Author: Koctr


# 类的析构方法


class Role(object):
    """ 演示析构方法"""
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("del...run...")

r = Role('test')
# 执行del同时执行析构方法
del r
