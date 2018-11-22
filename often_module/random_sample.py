# -*- coding: utf-8 -*-
__author__ = 'K0ctr'

import random

"""
random.random(): (0,1]之间的随机浮点数
"""
print(random.random())

"""
random.randint(i, j): [i,j]之间的整数
"""
print(random.randint(-11, 100))

"""
random.randrange(i, j): [i,j)之间的整数
"""
print(random.randrange(-50, 22, 2))

"""
random.randrange(i): [0,i)之间的整数
"""
print(random.randrange(100))

"""
random.choice(seq): 从序列中随机返回一个元素
"""
print(random.choice("abcdefghijk"))

"""
random.shuffle(x): 对输入的参数进行乱序排列
str是不能乱序的，请思考为什么？
"""
a_list = [1, 2, 3, 4, 5]
random.shuffle(a_list)
print(a_list)

byte = bytearray("abcdefg", encoding="utf-8")
random.shuffle(byte)
print(byte.decode())

"""
random.simple(p, k): 返回p中的k个随机元素组成的列表
"""
print(random.sample([1, 2, 2, 3, 4, 5], 3))
print(random.sample("abcedefg", 5))

"""
random.uniform(i, j): 
if i < j:
    i + (j - i) * random.random()
"""
print(random.uniform(1, 10))
print(random.uniform(10, 1))

"""
四位验证码
"""
choice_code = ""
for i in range(4):
    if random.randrange(4) == i:
        tmp = str(random.randint(0, 9))
    else:
        tmp = chr(random.randint(65, 90))
    choice_code += tmp
print(choice_code)
