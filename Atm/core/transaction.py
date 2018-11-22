# -*- encoding:utf-8 -*-
# Author: Koctr


from conf import settings
from core import account_manage


def make_transaction(logger, account_data, transaction_type, amount):
    """
    处理所有用户操作
    :param logger: 日志对象
    :param account_data: 账户数据
    :param transaction_type: 操作类型
    :param amount: 金额
    :return: 完成操作后的账户数据
    """
    amount = float(amount)
    new_credit = 0
    new_balance = 0
    if transaction_type in settings.TRANSACTION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[transaction_type]['interest']
        old_credit = account_data['credit']
        if settings.TRANSACTION_TYPE[transaction_type]['credit'] == 'plus':
            new_credit = old_credit + amount + interest
        elif settings.TRANSACTION_TYPE[transaction_type]['credit'] == 'minus':
            new_credit = old_credit - amount - interest
            if new_credit < 0:
                print('\33[31;1m你的额度 [%s] 不足以办理金额为 [%s] 的业务，你的余额为 [%s]\33[0m'
                      % (account_data['credit'], (amount + interest), account_data['balance']))
                return

        old_balance = account_data['balance']
        if settings.TRANSACTION_TYPE[transaction_type]['balance'] == 'plus':
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[transaction_type]['balance'] == 'minus':
            new_balance = old_balance - amount - interest

        account_data['balance'] = new_balance
        account_data['credit'] = new_credit
        account_manage.dump_account_data(account_data)
        logger.info('account: %s  action: %s  amount: %s  interest:  %s'
                    % (account_data['id'], settings.ACCOUNT_OPERATE[transaction_type], amount, interest))
        return account_data
    else:
        print('\33[31;1m业务类型 [%s] 无效。\33[0m' % transaction_type)
