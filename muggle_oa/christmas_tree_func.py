# -*- encoding:utf-8 -*-
# Author: Koctr


# 叶子层数
leaf_line = int(input("请输入树叶层数："))
# 叶子类型
leaf = input("请输入树叶类型：")
# 树干高度
trunk_high = int(input("请输入树干高度："))
# 树干字符
trunk = "|"

# 最大叶子数
max_leaf = leaf_line + leaf_line - 1
for i in range(1, leaf_line + 1):
    print(((i + i - 1) * leaf).center(max_leaf))
for i in range(0, trunk_high):
    print(trunk.center(max_leaf))
