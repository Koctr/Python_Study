# -*- coding:utf-8 -*-
# Author: Koctr


"""
使用函数模拟实现人和狗的各自动作
"""


def dog(name, dog_type):
    """狗"""
    data = {
        "name": name,
        "type": dog_type
    }
    return data


def person(name, age, sex, job):
    """人"""
    data = {
        "name": name,
        "age": age,
        "sex": sex,
        "job": job
    }
    return data


def bark(d):
    """狗叫"""
    print("dog %s wang wang wang..." % d["name"])


def walk(p):
    """人走"""
    print("person %s is warking" % p["name"])


d1 = dog("赛虎", "京巴")
bark(d1)

p1 = person("林海峰", 21, "F", "teacher")
p2 = person("孙海涛", 36, "F", "运维")
walk(p1)

# 方法可能误调用
bark(p1)
