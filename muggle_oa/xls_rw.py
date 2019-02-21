# -*- coding:utf-8 -*-
# Author: Koctr


import xlrd
import xlwt

workbook = xlrd.open_workbook("D:/7月下旬入库表.xlsx")
sheet = workbook.sheet_by_name("7月下旬入库表")
new_workbook = xlwt.Workbook()
new_sheet = new_workbook.add_sheet("7月下旬入库表")
for row in range(0, sheet.nrows):
    for col in range(0, sheet.ncols):
        new_sheet.write(row, col, sheet.cell_value(row, col))
# 保存成xlsx，office 2016无法打开
new_workbook.save("D:/new_book.xls")
