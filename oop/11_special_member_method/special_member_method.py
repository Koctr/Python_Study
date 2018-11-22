# -*- coding:utf-8 -*-
# Author: Koctr


class Dog(object):
    """__doc__方法显示这里的内容"""

    def __init__(self, name):
        self.name = name
        self.data = dict()

    def __call__(self, *args, **kwargs):
        # 对象后面再加括号来执行
        print('running call', args, kwargs)

    def __str__(self):
        return "toString"

    def __getitem__(self, key):
        print("__getitem__", key)
        return self.data.get(key)

    def __setitem__(self, key, value):
        print("__setitem__", key, value)
        self.data[key] = value

    def __delitem__(self, key):
        print("__delitem__", key)


print("__doc__", Dog.__doc__)
obj = Dog("wc")
# 输出当前对象是那个模块中的
print("__module__", obj.__module__)
# 输出类本身
print("__class__", obj.__class__)
# 执行call方法
obj(1, 2, 3, name=456)
# 查看类的所有成员
print("class __dict__", Dog.__dict__)
# 查看对象的所有成员
print("instance __dict__", obj.__dict__)
# 打印对象时输出__str__的内容
print("__str__", obj)
# setitem
obj["name"] = "alex"
# getitem
alex = obj["name"]
# delitem
del obj["name"]
