# -*- coding:utf-8 -*-
# Author: Koctr


import json

"""json序列化"""
f = open("json.txt", "w")
info = {"name": "alex",
        "age": 22}
f.write(json.dumps(info))
f.close()

"""json反序列化"""
f = open("json.txt", "r")
data = json.loads(f.read())
f.close()
print(data["age"])
