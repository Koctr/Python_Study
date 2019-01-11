# -*- coding:utf-8 -*-
# Author: Koctr

import os
import sys
import time

"""
程序规则：
1、输入目录
2、判断是否是目录，进入目录，遍历里面的文件
3、跳过目录
4、对每个文件，将文件改名为'出处-日期-文件名'的格式，出处指人名或部门，日期格式为yyyy-mm-dd
4.1、按照-split文件名，如果为4个以上元素
4.1.1、（针对目前'日期-文件名-出处’格式的文件）将前三个元素合并，判断是否为日期，不是日期转到4.2
4.1.2、是日期，将日期放在最后，最后一个元素放在最前面，中间的元素位置不变，以-分隔组合为新文件名
4.2、将后三个元素组合，判断是否为日期
4.2.1、是日期，将日期放在最前面，组合文件名
4.2.2、不是日期，则由文件的创建时间生成日期，将文件名改为‘日期-内容’的格式
4.3、如果是4个元素，执行4.2的步骤
4.4、如果是一个元素，执行4.2.2的步骤
"""


def run():
    """
    自动重命名程序入口
    :return:
    """
    argv = sys.argv
    if len(argv) != 2:
        print("程序调用方式不正确，输入格式为：'python auto_rename 目录或文件的路径'。")
    else:
        # 使用命令行传参时，不能使用单引号，否则无法识别为目录
        renames(argv[1])


def renames(path):
    if os.path.isdir(path):
        for dirs in os.listdir(path):
            for dir in dirs:
                if os.path.isfile(dir):
                    check_items(dir)
    elif os.path.isfile(path):
        print("This is a file.")
    else:
        print("目录或文件路径输入有错误。")


def check_items(file_path):
    path_and_name = os.path.split()
    str_list=path_and_name[1].split("-")
    if len(str_list) >= 5:
        pass
    if len(str_list) ==4:
        pass
    else:
        create_time = os.path.getctime(file_path)
        format_time = time.strftime('%Y-%m-%d', time.localtime(create_time))
        file_new_name = os.path.join(path_and_name[0],"%s-%s" %(format_time,path_and_name[1]))
        os.rename(file_path, file_new_name)
