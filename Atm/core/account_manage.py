# -*- encoding:utf-8 -*-
# Author: Koctr


import json
import os
from conf import settings
from core import db_handler


def load_account_data(account_id):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s.json' % (db_path, account_id)
    if os.path.isfile(account_file):
        with open(account_file, 'r', encoding="utf-8") as f:
            account_data = json.load(f)
            return account_data
    else:
        print('账户文件不存在')


def dump_account_data(account_data):
    db_path = db_handler.db_handler(settings.DATABASE)
    account_file = '%s/%s.json' % (db_path, account_data['id'])
    with open(account_file, 'w', encoding='utf-8') as f:
        json.dump(account_data, f)
        return True
