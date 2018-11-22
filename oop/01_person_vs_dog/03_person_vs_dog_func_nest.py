# -*- coding:utf-8 -*-
# Author: Koctr


"""使用嵌套函数避免函数误调用"""


def dog(name, dog_type):
    """狗"""
    def bark(d):
        """狗叫"""
        print("dog %s wang wang wang" % d["name"])

    data = {
        "name": name,
        "type": dog_type,
        "bark": bark
    }
    return data


def person(name, age, sex, job):
    """人"""
    def walk(p):
        """人走"""
        print("person %s is walking..." % p["name"])

    data = {
        "name": name,
        "age": age,
        "sex": sex,
        "job": job,
        "walk": walk
    }
    return data


d1 = dog("赛虎", "京巴")
d1["bark"](d1)

p1 = person("林海峰", 21, "F", "teacher")
p2 = person("孙海涛", 36, "F", "运维")
p1["walk"](p1)
