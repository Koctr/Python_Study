# -*- encoding:utf-8 -*-
# Author: Koctr


class Dog(object):
    """属性方法演示"""

    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        """将一个方法变为一个属性"""
        print("%s is eating %s" % (self.name, self.__food))
        return 1

    @eat.setter
    def eat(self, food):
        """给属性方法传参数"""
        print("Set to food: ", food)
        self.__food = food

    @eat.deleter
    def eat(self):
        """删除属性中的参数"""
        del self.__food
        print("删完了")

d = Dog("ChenRonghua")
d.eat
d.eat = "baozi"
d.eat

del d.eat
