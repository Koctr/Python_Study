# -*- coding:utf-8 -*-
# Author: Koctr


class Dog(object):
    """演示反射"""
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        """吃"""
        print("%s is eating %s..." % (self.name, food))

def bulk(self):
    """叫"""
    print("%s is yelling..." % self.name)


d = Dog("NiuHanyang")

choice = input(">>:").strip()

# 判断是否有方法
if hasattr(d, choice):
    # 得到方法的内存地址
    func = getattr(d, choice)
    func("egg")
    # 设置属性
    # attr = getattr(d. choice)
    # setattr(d, choice, "Ronghua")
    # print(getattr(d, choice))
    # 删除属性或方法
    # delattr(d, choice)
else:
    # 将一个函数动态设置为对象的方法，输入的是talk，就使用talk调用bulk函数
    # d.talk = bulk
    setattr(d, choice, bulk)
    func = getattr(d, choice)
    func()
    # 动态添加一个属性
    # setattr(d, choice, 22)
    # print(getattr(d, choice))
# 验证是否删除
# print(d.name)