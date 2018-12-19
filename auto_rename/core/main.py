# -*- coding:utf-8 -*-
# Author: Koctr

import os
import sys


"""
程序规则：
1、输入目录
2、判断是否是目录，进入目录，遍历里面的path
3、如果path是目录，跳过
4、如果path是文件，要将文件改名为'出处-日期-文件名'的格式，出处指人名或部门，日期格式为yyyy-mm-dd
4.1、针对目前'日期-文件名-出处’格式的文件
4.1.1、查找第三个-，切片前边的内容，判断是否为日期，不是日期转到4.2
4.1.2、是日期，查找第四个-，切片前后的内容（后面的内容是出处），将前后内容交换并加-，组合为新文件名
4.2、按照-，逐个截取，判断前后是否为日期，全部不是日期，则由文件的创建时间生成日期，将文件名改为‘日期-内容’的格式
"""


def run():
    """
    自动重命名程序入口
    :return:
    """
    argv=sys.argv
    if len(argv)!=2:
        print("程序调用方式不正确，输入格式为：'python auto_rename 目录或文件的路径'。")
    else:
        # 使用命令行传参时，不能使用单引号，否则无法识别为目录
        renames(argv[1])
        # os.walk()


def renames(path):
    if os.path.isdir(path):
        print("This is a path.")
    elif os.path.isfile(path):
        print("This is a file.")
    else:
        print("目录或文件路径输入有错误。")