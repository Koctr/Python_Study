# -*- coding:utf-8 -*-
# Author: Koctr


class Dog(object):
    """静态方法演示"""
    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat():
        """静态方法，与类没有关系，不能访问类的任何变量和方法"""
        print("dog is eating")

Dog.eat()
