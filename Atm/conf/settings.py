# -*- encoding:utf-8 -*-
# Author: Koctr


import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库配置
DATABASE = {
    'engine': 'file_storage',
    'name': 'accounts',
    'path': "%s/db" % BASE_DIR
}

# 正常账户
NORMAL_ACCOUNT = "normal"

# 被锁定账户
LOCKED_ACCOUNT = "locked"

# 被禁用账户
DISABLED_ACCOUNT = "disabled"

# 账户状态
ACCOUNT_STATUS = {
    NORMAL_ACCOUNT: 0,
    LOCKED_ACCOUNT: 1,
    DISABLED_ACCOUNT: 2,
}

# 表名列表
TABLE_NAMES = ['account_info']

# 列名列表
TABLE_COLUMNS = {
    'account_info': ['id', 'password', 'credit', 'balance', 'enroll_date', 'expire_date', 'pay_day', 'status']
}

# 列描述
COLUMN_COMMENT = {
    "id": "用户名",
    "password": '密码',
    'credit': '额度',
    'balance': '余额',
    'enroll_date': '创建日期',
    'expire_date': '过期日期',
    'pay_day': '账单日',
    'status': '状态',
}

# 账户操作
ACCOUNT_OPERATE = {
    'print_account_info': '打印账户信息',
    'repay': '还款',
    'withdraw': '取款',
    'transfer_out': '转出',
    'transfer_in': '转入',
    'consume': '消费',
}

# 日志级别
LOG_LEVEL = logging.INFO

# 日志类型
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}

# 操作类型
TRANSACTION_TYPE = {
    'repay': {'balance': 'minus', 'credit': 'plus', 'interest': 0},
    'withdraw': {'balance': 'plus', 'credit': 'minus', 'interest': 0.05},
    'transfer_out': {'balance': 'plus', 'credit': 'minus', 'interest': 0.05},
    'transfer_in': {'balance': 'minus', 'credit': 'plus', 'interest': 0},
    'consume': {'balance': 'plus', 'credit': 'minus', 'interest': 0},
}
