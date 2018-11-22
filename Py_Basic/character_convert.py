# -*- coding: utf-8 -*-
__author__ = 'K0ctr'


import chardet
import sys


print(sys.getdefaultencoding())

name = "张三"
print(chardet.detect(name.encode("gbk")))
print(chardet.detect(name.encode('utf-8')))
name_gbk = name.encode("gbk").decode("gbk")
print(name_gbk)
name_gb2312 = name_gbk.encode("gbk").decode("gbk").encode("gb2312").decode("gb2312")
print(name_gb2312)
