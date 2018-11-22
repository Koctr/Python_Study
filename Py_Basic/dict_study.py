# -*- encoding:utf-8 -*-
# Author: Koctr


info = {"id01": 1, "id02": 2, "id03": 3}

print(info.values())
print(info.keys())

item = info.setdefault("id01", 3)
print(item)

item = info.setdefault("id04", 4)
print(info)
