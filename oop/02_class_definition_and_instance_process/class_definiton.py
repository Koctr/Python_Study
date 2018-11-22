# -*- coding:utf-8 -*-
# Author: Koctr


# 定义类及实例化过程


class Dog(object):
    """定义狗这个类"""
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        """打招呼"""
        print("Hi, I am a dog. My name is ", self.name)

    def eat(self, food):
        """吃东西"""
        print("%s is eating %s." % (self.name, food))


# Dog(d1, "lichuang")
d1 = Dog("lichuang")
d2 = Dog("lichuang2")

# d1.say_hi(d1)
# self就是实例本身
d1.say_hi()
d2.say_hi()
