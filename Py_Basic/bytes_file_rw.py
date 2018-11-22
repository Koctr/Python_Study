# -*- coding: utf-8 -*-
__author__ = 'K0ctr'

filedata = b''
with open("flag.jpg", "rb") as jpg:
    filedata = jpg.read()
    filedata = filedata[::-1]

with open("flag.png", "wb") as png:
    png.write(filedata)
