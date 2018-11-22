# -*- encoding:utf-8 -*-
# Author: Koctr

# 将对象转换为字符串
a_list = [1, 2, 3, 4, 5]
iterator = iter(a_list)
print(type(iterator))
print(type(repr(iterator)))
