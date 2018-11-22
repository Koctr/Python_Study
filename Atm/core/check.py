# -*- encoding:utf-8 -*-
# Author: Koctr


import time
import os
import re
import datetime
from core import auth
from core import db_handler
from conf import settings


def check_valid_date(sdate):
    """
    验证字符串是否为日期格式（yyyy-mm-dd）
    :param sdate: 待验证的字符串
    :return: 验证结果
    """
    try:
        time.strptime(sdate, "%Y-%m-%d")
        return True
    except:
        print('\33[31;1m输入的日期 [%s] 格式不正确\33[0m' % sdate)
        return False


def check_valid_time(stime, limit_time):
    """
    验证时间是否符合要求
    :param stime: 待验证的时间字符串
    :param limit_time: 限制时间，待验证时间要大于等于限制时间
    :return: 
    """
    if check_valid_date(stime):
        if stime <= '1970-1-1':
            print('\33[31;1m日期 [%s] 超出时间范围\33[0m' % stime)
        else:
            stime_time = time.mktime(time.strptime(stime, '%Y-%m-%d'))
            if stime_time < limit_time:
                print('\33[31;1m日期 [%s] 应在 [%s]之后\33[0m' % (stime, time.strftime('%Y-%m-%d',
                                                                                 time.localtime(limit_time))))
            else:
                return True


def check_user_is_login(logger, user_type, session_data):
    """
    装饰器，判断是否登录，如果未登录，根据登录用户类型调用不同的登录函数    
    :param logger: 日志对象
    :param user_type: 用户登录类型（manager，another）
    :param session_data: 用户数据
    :return: 外层装饰器
    """
    def outter_wrapper(func):
        """
        外层装饰器
        :param func: 被装饰的函数名
        :return: 里层装饰器
        """
        def wrapper(*args, **kwargs):
            """
            装饰器
            :param args: 被装饰函数参数
            :param kwargs: 被装饰函数参数
            :return: 被装饰函数的返回值
            """
            if not session_data['is_authenticated']:
                if user_type == 'manager':
                    auth.manager_login(logger, session_data)
                    if session_data['is_authenticated']:
                        return func(*args, **kwargs)
                else:
                    account_data = auth.account_login(logger, session_data)
                    if session_data['is_authenticated']:
                        session_data['account_data'] = account_data
                        return func(*args, **kwargs)
            else:
                return func(*args, **kwargs)
        return wrapper
    return outter_wrapper


def check_account_data(account_data):
    """
    验证账户数据有效性
    :param account_data: 账户数据
    :return: 账户有效性
    """
    flag = True
    if account_data['id']:
        if not check_username(account_data['id']):
            flag = False
        else:
            db_path = db_handler.db_handler(settings.DATABASE)
            account_file = '%s/%s.json' % (db_path, account_data['id'])
            if os.path.isfile(account_file):
                print('\33[31;1m%s [%s] 已存在\33[0m' % (settings.COLUMN_COMMENT['id'], account_data['id']))
                flag = False
    else:
        print('\33[31;1m%s不能为空\33[0m' % settings.COLUMN_COMMENT['id'])
        flag = False

    if not account_data['password']:
        print('\33[31;1m%s不能为空\33[0m' % settings.COLUMN_COMMENT['password'])
        flag = False

    credit = account_data['credit']
    if credit:
        if not credit.isdigit():
            print('\33[31;1m%s应为正整数\33[0m' % settings.COLUMN_COMMENT['credit'])
            flag = False
        else:
            if int(credit) <= 0:
                print('\33[31;1m%s应为正整数\33[0m' % settings.COLUMN_COMMENT['credit'])
                flag = False
            else:
                account_data['credit'] = int(credit)
    else:
        print('\33[31;1m%s不能为空\33[0m' % settings.COLUMN_COMMENT['credit'])
        flag = False

    balance = account_data['balance']
    if balance:
        if not balance.isdigit() or (balance.isdigit() and int(balance) != 0):
            print('\33[31;1m%s应为0\33[0m' % settings.COLUMN_COMMENT['balance'])
            flag = False
        else:
            account_data['balance'] = 0
    else:
        account_data['balance'] = 0

    enroll_date = account_data['enroll_date']
    if enroll_date:
        yesterday = datetime.datetime.timestamp(datetime.datetime.today() - datetime.timedelta(days=1))
        if not check_valid_time(enroll_date, yesterday):
            flag = False
    else:
        account_data['enroll_date'] = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    expire_date = account_data['expire_date']
    if expire_date:
        if not check_valid_time(expire_date, time.time()):
            flag = False
    else:
        print('\33[31;1m%s不能为空\33[0m' % settings.COLUMN_COMMENT['expire_date'])

    pay_day = account_data['pay_day']
    if pay_day:
        if not pay_day.isdigit() or (pay_day.isdigit and (int(pay_day) == 0 or int(pay_day) > 28)):
            print('\33[31;1m%s必须在1-28之间\33[0m' % settings.COLUMN_COMMENT['pay_day'])
            flag = False
        else:
            account_data['pay_day'] = int(pay_day)
    else:
        print('\33[31;1m%s必须在1-28之间\33[0m' % settings.COLUMN_COMMENT['pay_day'])
        flag = False

    status = account_data['status']
    if status:
        if not status.isdigit() or (status.isdigit() and int(status) not in list(settings.ACCOUNT_STATUS.values())):
            print('\33[31;1m%s必须在%s中\33[0m' % (settings.COLUMN_COMMENT['status'],
                                               list(settings.ACCOUNT_STATUS.values())))
            flag = False
        else:
            account_data['status'] = int(status)
    else:
        account_data['status'] = settings.ACCOUNT_STATUS[settings.NORMAL_ACCOUNT]

    return flag


def check_username(username):
    """
    验证用户名合规性
    :param username: 用户名
    :return: 是否合规
    """
    is_invalid_username = re.search('[\W]+', username)
    if is_invalid_username:
        print('\33[31;1m账号名 [%s] 非法，只能包含字母数字和下划线\33[0m' % username)
    else:
        return True
