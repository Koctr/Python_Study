# -*- encoding:utf-8 -*-
# Author: Koctr


# 总行数
line = 6
# 叶子行数
leaf_line = 4
# 最大叶子树
max_leaf = 7
# 叶子字符
leaf = "*"
# 树干字符
trunk = "|"
# 叶子增量
increment = 0
for i in range(1, line + 1):
    if i <= leaf_line:
        print(((i + increment) * leaf).center(max_leaf))
        increment = increment + 1
    else:
        print(trunk.center(max_leaf))
