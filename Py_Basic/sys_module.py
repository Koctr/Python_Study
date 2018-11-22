# -*- encoding:utf-8 -*-
# Author: Koctr


import sys


print(sys.path)

args = sys.argv
if len(args) > 1:
    print(args[1])
else:
    print("没有参数")
