# -*- coding:utf-8 -*-
# Author: Koctr

import xlrd
import xlsxwriter
import pymysql

database = pymysql.connect("127.0.0.1", "root", "root", "muggle_oa", charset="utf8")
cursor = database.cursor()
sql = "select company,count(weight),sum(weight),sum(weight*price) from data group by company"
cursor.execute(sql)
result = cursor.fetchall()
database.close()

xls = xlrd.open_workbook(r"D:\7月下旬统计表.xls")
sheet = xls.sheet_by_index(0)

new_xls = xlsxwriter.Workbook(r"D:\7月下旬统计表1.xlsx")
new_sheet = new_xls.add_worksheet("Sheet1")
new_sheet.write(0, 0, sheet.row(0)[0].value)
new_sheet.write(1, 0, sheet.cell_value(1, 0))
new_sheet.write(1, 1, sheet.cell_value(1, 1))
new_sheet.write(1, 2, sheet.cell_value(1, 2))
new_sheet.write(1, 3, sheet.cell_value(1, 3))
for data in result:
    for row in range(2, sheet.nrows):
        if data[0] == sheet.cell_value(row, 0):
            new_sheet.write(row, 0, sheet.cell(row, 0).value)
            new_sheet.write(row, 1, data[1])
            new_sheet.write(row, 2, data[2])
            new_sheet.write(row, 3, data[3])
new_xls.close()
