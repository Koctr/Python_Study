# -*- encoding:utf-8 -*-
# Author: Koctr


class MyType(type):
    def __init__(cls, what, bases=None, dict=None):
        print("MyType init.")
        super(MyType, cls).__init__(what, bases, dict)

    def __call__(cls, *args, **kwargs):
        print("MyType call.")
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(obj, *args, **kwargs)


class Foo(object):
    __metaclass__ = MyType

    def __init__(self, name):
        self.name = name
        print("Foo init.")

    def __new__(cls, *args, **kwargs):
        """__new__是用来创建实例的"""
        print("Foo new.")
        return object.__new__(cls)

obj = Foo("Koctr")
