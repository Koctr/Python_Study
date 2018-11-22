# -*- coding:utf-8 -*-
# Author: Koctr


"""
使用函数模拟人狗大战，实现各自的属性
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

d1 = dog("赛虎", "京巴")

p1 = person("林海峰", 21, "F", "teacher")
p2 = person("孙海涛", 36, "F", "运维")

print(d1["type"])
