# -*- encoding:utf-8 -*-
# Author: Koctr

d = {1: 2, 99: 100, 4: -1, 5: 30, -2: 88}
print(d)
print(sorted(d))
print(type(sorted(d.items())))
print(sorted(d.items(), key=lambda x: x[1]))
