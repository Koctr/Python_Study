# -*- coding:utf-8 -*-
# Author: Koctr


class MyError(Exception):
    """自定义异常"""
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    raise MyError("数据库连接异常")
except MyError as e:
    print(e)
