# -*- coding:utf-8 -*-
# Author: Koctr


import shutil
import os

with open("text1", "w", encoding="utf-8") as f1:
    f1.write("Hello World!")

with open("text1", "r", encoding="utf-8") as f1, open("text2", "w", encoding="utf-8") as f2:
    shutil.copyfileobj(f1, f2)

with open("text3", "w", encoding="utf-8") as f3:
    f3.write("Koctr")

"""
自动生成text4
"""
shutil.copyfile("text3", "text4")

"""
拷贝权限，Linux下有用
"""
shutil.copymode("text3", "text4")

"""
拷贝状态
"""
shutil.copystat("text3", "text4")

"""
拷贝内容和权限
"""
shutil.copy("text3", "text4")

"""
拷贝内容和状态
"""
shutil.copy2("text3", "text4")

"""
递归拷贝，默认使用copy2？
"""
shutil.copytree(r"a", r"e")

shutil.rmtree("e")

"""
shutil.make_archive(path, format(zip,tar,bztar,gztar),dir,owner,group,logger)
"""
shutil.make_archive("shutil_archive_test", "zip", "E:\c_study")
os.remove("shutil_archive_test.zip")
