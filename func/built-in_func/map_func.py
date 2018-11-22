# -*- encoding:utf-8 -*-
# Author: Koctr

for b in map(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]):
    print(b)

for s in map(str, [1, 2, 3, 4, 5]):
    print(type(s), s)
