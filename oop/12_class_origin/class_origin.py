# -*- coding:utf-8 -*-
# Author: Koctr


def func(self):
    print("Hello, %s." % self.name)


def __init__(self, name):
    self.name = name

Foo = type("Foo", (object,), {'talk': func, '__init__': __init__})

f = Foo("Koctr")
f.talk()
# Foo是type的对象
# type是类的类
print(type(Foo))
