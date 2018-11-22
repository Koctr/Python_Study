# -*- encoding:utf-8 -*-
# Author: Koctr

# zip(*iterables)

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd']

print(type(zip(a, b)))
for i in zip(a, b):
    print(i)
