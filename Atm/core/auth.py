# -*- encoding:utf-8 -*-
# Author: Koctr


import os
import json
import time
from core import db_handler
from core import check
from conf import settings


def account_auth(account, password):
    """
    账户验证
    :param account: 账户名
    :param password: 账户密码
    :return: 账户数据
    """
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s.json' % (db_path, account)
    if os.path.isfile(account_file):
        with open(account_file, 'r', encoding="utf-8") as f:
            account_data = json.load(f)
            if account_data['password'] == password:
                expire_time_stamp = time.mktime(time.strptime(account_data['expire_date'], '%Y-%m-%d'))
                if time.time() > expire_time_stamp:
                    print('\33[31;1m账号 %s 已过期，请联系取得新卡\33[0m' % account)
                elif account_data['status'] == settings.ACCOUNT_STATUS[settings.LOCKED_ACCOUNT]:
                    print('\33[31;1m账号 %s 已锁定，请联系解锁\33[0m' % account)
                elif account_data['status'] == settings.ACCOUNT_STATUS[settings.DISABLED_ACCOUNT]:
                    print('\33[31;1m账号 %s 已禁用，请联系解禁\33[0m' % account)
                else:
                    return account_data
            else:
                print('\33[31;1m账号或密码错误\33[0m')
    else:
        print('\33[31;1m账号 %s 不存在\33[0m' % account)


def account_login(logger, user_data):
    """
    账户登录
    :param logger: longging对象
    :param user_data: 用户session
    :return: 账户数据
    """
    retry_count = 0
    account = ''
    while retry_count < 3:
        account = input('\33[32;1m请输入账号：\33[0m').strip()
        password = input('\33[32;1m请输入密码：\33[0m').strip()
        is_valid_name = check.check_username(account)
        if is_valid_name:
            account_data = account_auth(account, password)
            if account_data:
                user_data['account_id'] = account_data['id']
                # 装饰器要求必须在这里设置用户是否已验证
                user_data['is_authenticated'] = True
                return account_data
        retry_count += 1
    else:
        logger.error('账号 [%s] 尝试登录次数过多' % account)


def manager_login(logger, manager_data):
    """
    管理员登录
    :param logger: logging对象
    :param manager_data: 管理员session
    :return: 登录是否成功
    """
    retry_count = 0
    manager = ''
    while retry_count < 3:
        manager = input('\33[32;1m请输入账号：\33[0m').strip()
        password = input('\33[32;1m请输入密码：\33[0m').strip()
        is_valid_name = check.check_username(manager)
        if is_valid_name:
            if manager_auth(manager, password):
                # 装饰器要求必须在这里设置用户是否已验证
                manager_data['is_authenticated'] = True
                return True
        retry_count += 1
    else:
        logger.error('账号 [%s] 尝试登录次数过多' % manager)


def manager_auth(manager, password):
    """
    管理员验证
    :param manager: 管理员用户名
    :param password: 密码
    :return: 验证结果
    """
    manager_file = '%s/db/manager/%s.json' % (settings.BASE_DIR, manager)
    print(manager_file)
    if os.path.isfile(manager_file):
        with open(manager_file, 'r', encoding="utf-8") as f:
            manager_data = json.load(f)
            if manager_data['password'] == password:
                return True
            else:
                print('\33[31;1m账号或密码错误\33[0m')
    else:
        print('\33[31;1m账号 %s 不存在\33[0m' % manager)
