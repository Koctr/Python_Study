# -*- encoding:utf-8 -*-
# Author: Koctr


import re
from core import account_manage
from core import transaction
from core import logger
from core import check
from core import auth
from conf import settings


# 根据类型建立不同的日志对象
transaction_logger = logger.log("transaction")
access_logger = logger.log("access")

# 账户session
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'account_data': None,
}

# 管理员session
manager_data = {
    'is_authenticated': False
}


def run():
    """
    账户入口
    :return: 无
    """
    account_data = auth.account_login(access_logger, user_data)
    if user_data['is_authenticated']:
        user_data['account_data'] = account_data
        interactive(user_data)


def manage_run():
    """
    管理员入口
    :return: 无
    """
    auth.manager_login(access_logger, manager_data)
    if manager_data['is_authenticated']:
        manage()


@check.check_user_is_login(access_logger, 'manager', manager_data)
def manage():
    """
    管理菜单
    :return: 无
    """
    menu = '''
    --------管理菜单------
    \33[32;1m1. 创建账户
    2. 修改额度
    3. 冻结账户
    4. 禁用账户
    5. 启用账户
    6. 退出
    \33[0m
    '''
    menu_dic = {
        '1': create_account,
        '2': update_credit,
        '3': lock_account,
        '4': disable_account,
        '5': enable_or_unlock_account,
        '6': manage_logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input("输入数字选择菜单:").strip()
        if user_option in menu_dic:
            menu_dic[user_option]()
        else:
            print('\33[31;1m无效的选择\33[0m')


@check.check_user_is_login(access_logger, 'account', user_data)
def interactive(acc_data):
    """
    账户菜单
    :param acc_data: 账户会话
    :return: 无
    """
    menu = '''
    --------用户菜单--------
    \33[32;1m1. 打印账户信息
    2. 还款
    3. 取款
    4. 转账
    5. 账单
    6. 退出
    \33[0m
    '''
    menu_dic = {
        '1': print_account_info,
        '2': repay,
        '3': withdraw,
        '4': transfer,
        '5': pay_check,
        '6': logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input("输入数字选择菜单:").strip()
        if user_option in menu_dic:
            menu_dic[user_option](acc_data)
        else:
            print('\33[31;1m无效的选择\33[0m')


@check.check_user_is_login(access_logger, 'account', user_data)
def print_account_info(acc_data):
    """
    打印账户信息
    :param acc_data: 账户session
    :return: 无
    """
    account_data = account_manage.load_account_data(acc_data['account_id'])
    if account_data:
        print("账户信息：")
        for key in account_data:
            print('%s: %s' % (settings.COLUMN_COMMENT[key], account_data[key]))


@check.check_user_is_login(access_logger, 'account', user_data)
def repay(acc_data):
    """
    还款
    :param acc_data: 账户session
    :return: 无
    """
    account_data = account_manage.load_account_data(acc_data['account_id'])
    if account_data:
        current_balance_and_credit = '你的当前余额为 [%s]，当前额度为 [%s]' \
                                     % (account_data['balance'], account_data['credit'])
        print(current_balance_and_credit)

        back_flag = False
        while not back_flag:
            repay_amount = input('\33[33;1m请输入还款金额（输入b返回主菜单）：\33[0m').strip()
            if repay_amount.lower() == 'b':
                back_flag = True
            else:
                is_positive_number = re.match('^(([0-9]+[.]?[0-9]+)|[1-9])$', repay_amount)
                if is_positive_number and float(is_positive_number.group()) != 0.0:
                    new_account_data = transaction.make_transaction(transaction_logger, account_data, 'repay', repay_amount)
                    if new_account_data:
                        account_data = new_account_data
                        print('\33[42;1m你新的余额为 [%s]，额度为 [%s]\33[0m'
                              % (account_data['balance'], account_data['credit']))
                else:
                    print('\33[31;1m还款金额 [%s] 不是正数。\33[0m' % repay_amount)


@check.check_user_is_login(access_logger, 'account', user_data)
def withdraw(acc_data):
    """
    取现
    :param acc_data: 账户session
    :return: 无
    """
    account_data = account_manage.load_account_data(acc_data['account_id'])
    if account_data:
        current_balance_and_credit = '你的当前余额为 [%s]，当前额度为 [%s]' \
                                     % (account_data['balance'], account_data['credit'])
        print(current_balance_and_credit)

        back_flag = False
        while not back_flag:
            withdraw_amount = input('\33[33;1m请输入取现金额（输入b返回主菜单）：\33[0m').strip()
            if withdraw_amount.lower() == 'b':
                back_flag = True
            else:
                # 会匹配0.0
                is_positive_number = re.match('^(([0-9]+[.]?[0-9]+)|[1-9])$', withdraw_amount)
                if is_positive_number and float(is_positive_number.group()) != 0.0:
                    new_account_data = transaction.make_transaction(transaction_logger, account_data, 'withdraw',
                                                                    withdraw_amount)
                    if new_account_data:
                        account_data = new_account_data
                        print('\33[42;1m你新的余额为 [%s]，额度为 [%s]\33[0m'
                              % (account_data['balance'], account_data['credit']))
                else:
                    print('\33[31;1m取现金额 [%s] 应为正数\33[0m' % withdraw_amount)


@check.check_user_is_login(access_logger, 'account', user_data)
def transfer(acc_data):
    """
    转账
    :param acc_data: 账户session
    :return: 无
    """
    account_data = account_manage.load_account_data(acc_data['account_id'])
    if account_data:
        current_balance_and_credit = '你的当前余额为 [%s]，当前额度为 [%s]' \
                                     % (account_data['balance'], account_data['credit'])
        print(current_balance_and_credit)

        back_flag = False
        while not back_flag:
            account_and_amount = input('\33[33;1m请输入转账用户及金额，以逗号分隔（输入b返回主菜单）：\33[0m').\
                strip()
            if account_and_amount.lower() == 'b':
                back_flag = True
            else:
                account_and_amount_list = account_and_amount.split(',')
                if len(account_and_amount_list) != 2:
                    print('\33[31;1m转账用户及金额 [%s] 输入格式不正确\33[0m' % account_and_amount)
                else:
                    transfer_account_id = account_and_amount_list[0].strip()
                    if transfer_account_id == account_data['id']:
                        print('\33[31;1m不能给自己转账\33[0m')
                    elif not check.check_username(transfer_account_id):
                        pass
                    else:
                        transfer_account_data = account_manage.load_account_data(transfer_account_id)
                        if transfer_account_data:
                            transfer_amount = account_and_amount_list[1].strip()
                            is_positive_number = re.match('^(([0-9]+[.]?[0-9]+)|[1-9])$', transfer_amount)
                            if is_positive_number and float(is_positive_number.group()) != 0.0:
                                new_account_data = transaction.make_transaction(transaction_logger, account_data,
                                                                                'transfer_out', transfer_amount)
                                if new_account_data:
                                    account_data = new_account_data
                                    transaction.make_transaction(transaction_logger, transfer_account_data, 'transfer_in',
                                                                 transfer_amount)
                                    print('\33[42;1m你新的余额为 [%s]，额度为 [%s]\33[0m'
                                          % (account_data['balance'], account_data['credit']))
                            else:
                                print('\33[31;1m转账金额 [%s] 应为正数\33[0m' % transfer_amount)


@check.check_user_is_login(access_logger, 'account', user_data)
def pay_check(acc_data):
    """
    打印账单
    :param acc_data: 账户会话
    :return: 无
    """
    account_data = account_manage.load_account_data(acc_data['account_id'])
    if account_data:
        current_balance_and_credit = '你的当前余额为 [%s]，当前额度为 [%s]' \
                                     % (account_data['balance'], account_data['credit'])
        print(current_balance_and_credit)

        back_flag = False
        while not back_flag:
            sdate = input('\33[33;1m请输入年月，格式为年-月-日（yyyy-mm-dd），输入b返回主菜单：\33[0m')\
                .strip()
            if sdate.lower() == 'b':
                back_flag = True
            else:
                is_valid_date = check.check_valid_date(sdate)
                if is_valid_date:
                    log_file = "%s/logs/%s" % (settings.BASE_DIR, settings.LOG_TYPES['transaction'])
                    with open(log_file, 'r') as f:
                        for line in f:
                            if sdate in line and account_data['id'] in line:
                                print(line.strip())


@check.check_user_is_login(access_logger, 'account', user_data)
def consume(account_amount):
    """
    消费
    :param account_amount: 消费金额
    :return: 无
    """
    # 参数：消费金额，直接调用user_data，不循环
    account_data = account_manage.load_account_data(user_data['account_id'])
    if account_data:
        current_balance_and_credit = '你的当前余额为 [%s], 额度为 [%s]\33' \
                                     % (account_data['balance'], account_data['credit'])
        print(current_balance_and_credit)
        new_account_data = transaction.make_transaction(transaction_logger, account_data, 'consume', account_amount)
        if new_account_data:
            account_data = new_account_data
            print('\33[42;1m你新的余额为 [%s]，额度为 [%s]\33[0m'
                  % (account_data['balance'], account_data['credit']))
            return True


def logout(acc_data):
    """
    退出系统
    :param acc_data: 账户session
    :return: 无
    """
    acc_data['account_id'] = None
    acc_data['is_authenticated'] = False
    acc_data['account_data'] = None
    print("再见")
    exit()


@check.check_user_is_login(access_logger, 'manager', manager_data)
def create_account():
    """
    创建账户
    :return: 无
    """
    back_flag = False
    while not back_flag:
        print('\33[33;1m要创建的账户信息包含的内容如下：\33[0m')
        print('\33[33;1m%s\33[0m' % ', '.join(settings.TABLE_COLUMNS['account_info']))
        data = input('\33[33;1m请输入账户信息，以逗号分隔（输入b返回主菜单）：\33[0m').strip()
        if data == 'b':
            back_flag = True
        else:
            data_list = data.split(',')
            if len(data_list) == len(settings.TABLE_COLUMNS['account_info']):
                for value in data_list:
                    data_list[data_list.index(value)] = value.strip()
                account_data = dict(zip(settings.TABLE_COLUMNS['account_info'], data_list))
                if check.check_account_data(account_data):
                    account_manage.dump_account_data(account_data)
                    print('\33[42;1m账户 [%s] 已创建\33[0m' % account_data['id'])
            else:
                print('\33[31;1m值不足或值太多\33[0m')


@check.check_user_is_login(access_logger, 'manager', manager_data)
def update_credit():
    """
    更新账户额度
    :return: 无
    """
    back_flag = False
    while not back_flag:
        account_and_credit = input('\33[33;1m请输入账号与额度，以逗号分隔（输入b返回主菜单）：\33[0m').strip()
        if account_and_credit == 'b':
            back_flag = True
        else:
            account_and_credit_list = account_and_credit.split(',')
            if len(account_and_credit_list) != 2:
                print('\33[31;1m输入的账号与额度 [%s] 格式不正确\33[0m' % account_and_credit)
            else:
                account_id = account_and_credit_list[0].strip()
                if check.check_username(account_id):
                    account_data = account_manage.load_account_data(account_id)
                    if account_data:
                        account_credit = account_and_credit_list[1].strip()
                        if account_credit.isdigit() and int(account_credit) > 0:
                            account_data['credit'] = int(account_credit)
                            account_manage.dump_account_data(account_data)
                            print('\33[42;1m账号 [%s] 额度修改为 [%s]\33[0m' % (account_id, account_credit))
                        else:
                            print('\33[31;1m额度 [%s] 应为正整数\33[0m' % account_credit)


@check.check_user_is_login(access_logger, 'manager', manager_data)
def lock_account():
    """
    锁定账户
    :return: 无
    """
    update_account_status('锁定', settings.ACCOUNT_STATUS[settings.LOCKED_ACCOUNT])


@check.check_user_is_login(access_logger, 'manager', manager_data)
def disable_account():
    """
        禁用账户
        :return: 无
        """
    update_account_status('禁用', settings.ACCOUNT_STATUS[settings.DISABLED_ACCOUNT])


@check.check_user_is_login(access_logger, 'manager', manager_data)
def enable_or_unlock_account():
    """
        启用账户
        :return: 无
        """
    update_account_status('启用', settings.ACCOUNT_STATUS[settings.NORMAL_ACCOUNT])


@check.check_user_is_login(access_logger, 'manager', manager_data)
def update_account_status(account_operate, account_status):
    """
    实现用户状态修改
    :param account_operate: 要修改的账户状态提示信息
    :param account_status: 要修改的账户状态
    :return: 
    """
    back_flag = False
    while not back_flag:
        account_id = input('\33[33;1m请输入要%s的账号名（输入b返回主菜单）：\33[0m' % account_operate).strip()
        if account_id == 'b':
            back_flag = True
        else:
            if check.check_username(account_id):
                account_data = account_manage.load_account_data(account_id)
                if account_data:
                    account_data['status'] = account_status
                    account_manage.dump_account_data(account_data)
                    print('\33[42;1m账号 [%s] 已%s\33[0m' % (account_id, account_operate))


def manage_logout():
    """
    退出管理
    :return: 无
    """
    print('再见')
    exit()
