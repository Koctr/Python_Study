# -*- coding:utf-8 -*-
# Author: Koctr


import xlrd
import xlsxwriter

workbook = xlrd.open_workbook("D:/7月下旬入库表.xlsx")
sheet = workbook.sheet_by_index(0)
new_workbook = xlsxwriter.Workbook("D:/new_book.xlsx")
new_sheet = new_workbook.add_worksheet("7月下旬入库表")
for row in range(0, sheet.nrows):
    for col in range(0, sheet.ncols):
        new_sheet.write(row, col, sheet.cell(row, col).value)
        # sheet.row(row)[col].value
new_workbook.close()
