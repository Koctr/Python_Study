# -*- encoding:utf-8 -*-
# Author: Koctr


def local_func():
    x = 5
    print(locals())
    print(x)


local_func()
print(globals())
