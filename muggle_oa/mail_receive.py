# -*- coding: utf-8 -*-
# author = 'K0ctr'


import zmail

server = zmail.server("koctr_2004@163.com", "iyclnmdb123.")
mails = server.get_mails('网易')

for mail in mails:
    print(mail['Subject'])
