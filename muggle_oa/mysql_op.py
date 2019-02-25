# -*- encoding:utf-8 -*-
# Author: Koctr


import pymysql

database = pymysql.connect("127.0.0.1", "root", "root", "muggle_oa", charset="utf8")
cursor = database.cursor()

sql = "select sum(weight) from data where company='王五小麦' and province='河北' " \
      "and date between '2018-7-21' and '2018-7-25'"
cursor.execute(sql)
result = cursor.fetchall()
print(result)
database.close()
