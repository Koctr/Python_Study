# -*- coding:utf-8 -*-
# Author: Koctr


import shelve
import datetime

"""shelve序列化"""

d = shelve.open("shelve.info")

info = {
    "name": "Alex",
    "age": 22
}

name = ["Koctr", "Koth"]

d["info"] = info
d["name"] = name
d["date"] = datetime.datetime.now()

d.close()

"""shelve反序列化"""
d = shelve.open("shelve.info")
print(d.get("info"))
print(d.get("name"))
print(d.get("date"))
