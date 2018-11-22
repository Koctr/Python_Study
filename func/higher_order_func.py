# -*- coding:utf-8 -*-
# Author: Koctr


def foo(func):
    func()
    print("the foo")


def boo():
    print("the boo")


foo(boo)


def foo1(func):
    print(func)
    return func


boo = foo1(boo)
boo()
