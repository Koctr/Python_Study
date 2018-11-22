# -*- coding:utf-8 -*-
# Author: Koctr


class Animal(object):
    """模拟多态"""
    def __init__(self, name):
        self.name = name

    def talk(self):
        """抽象方法"""
        raise NotImplementedError("Subclass must implement abstract method.")


class Dog(Animal):
    """狗"""
    def talk(self):
        """实现抽象方法"""
        return "Woof! woof!"


class Cat(Animal):
    """牛"""
    def talk(self):
        """实现抽象方法"""
        return "Meow!"


def animal_talk(obj):
    """使用函数模拟多态"""
    print(obj.talk())


c = Cat("C1")
d = Dog("D1")

animal_talk(c)
animal_talk(d)
