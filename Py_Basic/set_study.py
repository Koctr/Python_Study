# -*- encoding:utf-8 -*-
# Author: Koctr


list_1 = [1, 2, 23, 4, 5, 6, 4, 7]
set_1 = set(list_1)
print(set_1)

# a_set = set([1, 2, 3, 4, 5]) #这种声明方法可能被替换
set_2 = {1, 23, 98, 38, 12, 55}
set_3 = {15, 18, 99}
set_4 = {1,2}


print(set_1.intersection(set_2))
print(set_1 & set_2)

print(set_1.union(set_2))
print(set_1 | set_2)

print(set_1.difference(set_2))
print(set_1 - set_2)

print(set_4.issubset(set_1))
print(set_4 <= set_1)

print(set_1.issuperset(set_4))
print(set_1 >= set_4)

print(set_1.symmetric_difference(set_2))
print(set_1 ^ set_2)

print(set_1.isdisjoint(set_3))

set_1.add(3)
print(set_1)

set_1.update([1, 2, 3, 4, 5, 6, 7])
print(set_1)

set_1.remove(1)
print(set_1)

set_1.discard(1)
print(set_1)

item = set_1.pop()
print(item, set_1)
