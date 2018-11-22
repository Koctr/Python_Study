# -*- encoding:utf-8 -*-
# Author: Koctr


class Dog(object):
    """类方法演示"""

    # 类变量
    name = "Huazai"

    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        """类方法，只能访问类变量"""
        print("Dog %s is eating" % self.name)


Dog.eat()
