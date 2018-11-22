# -*- encoding:utf-8 -*-
# Author: Koctr


from collections import Iterable
from collections import Iterator

print(isinstance([1, 2, 3], Iterable))
print(isinstance(iter([1, 2, 3]), Iterator))

print(isinstance({1, 2, 3}, Iterable))
print(isinstance(iter({1, 2, 3}), Iterator))

a_set = {1, 2, 3, 1}
iterator = iter(a_set)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
