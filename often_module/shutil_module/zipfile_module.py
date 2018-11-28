# -*- coding:utf-8 -*-
# Author: Koctr


import zipfile

z = zipfile.ZipFile("test.zip", "w")
z.write("text3")
z.write("text4")
z.close()

z = zipfile.ZipFile("test.zip", "r")
z.extractall()
z.close()
