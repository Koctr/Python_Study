# -*- coding:utf-8 -*-
# Author: Koctr

import os
import sys
def run():
    """
    自动重命名程序入口
    :return:
    """
    path=sys.argv
    if len(path)!=2:
        print("请输入python auto_rename 目录或文件。")
    else:
        renames(path[1])


def renames(path):
    pass