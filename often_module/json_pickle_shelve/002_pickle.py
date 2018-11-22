# -*- coding:utf-8 -*-
# Author: Koctr


import pickle

"""pickle序列化"""


def say_hi():
    """
    用于序列化的函数
    :return: 无
    """
    print("Hello, world.")

info = {
    "name": "Alex",
    "age": 22,
    "func": say_hi
}

f = open("pick.info", "wb")
f.write(pickle.dumps(info))
f.close()

"""pickle反序列化"""
f = open("pick.info", "rb")
data = pickle.loads(f.read())
f.close()
data["func"]()

"""pickle使用dump方法序列化"""
f = open("pick.info", "wb")
pickle.dump(info, f)
f.close()

"""pickle使用load方法反序列化"""
f = open("pick.info", "rb")
data = pickle.load(f)
data["func"]()
f.close()
