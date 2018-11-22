# -*- encoding:utf-8 -*-
# Author: Koctr


import os
import pickle
from conf import settings


def check_data_valid(table_name, table_columns_and_values):
    """
    验证数据有效性
    :param table_name: 表名 
    :param table_columns_and_values: 列值字典
    :return: 验证结果
    """
    data_valid = True
    for key in table_columns_and_values:
        if settings.DATA_DICT[table_name][key][1] == int:
            if table_columns_and_values[key] and not table_columns_and_values[key].isdigit():
                print("列%s应为数字" % settings.DATA_DICT[table_name][key][2])
                data_valid = False
                break
        if len(table_columns_and_values[key]) > settings.DATA_DICT[table_name][key][0]:
            print("列%s值过大" % settings.DATA_DICT[table_name][key][2])
            data_valid = False
            break
    return data_valid


def load_file(table_name):
    """
    通过表名加载同名的piclke文件
    :param table_name: 表名
    :return: 取出的数据（字典）
    """
    data = dict()
    file_name = "%s/db/%s" % (settings.BASE_DIR, table_name)
    if os.path.isfile(file_name):
        with open(file_name, "rb") as f:
            data = pickle.load(f)
    return data


def save_file(table_name, data):
    """
    通过表名保存同名的picle文件
    :param table_name: 表名
    :param data: 要保存的数据（字典）
    :return: 是否成功保存
    """
    file_name = "%s/db/%s" % (settings.BASE_DIR, table_name)
    with open(file_name, "wb") as f:
        pickle.dump(data, f)
        return True
