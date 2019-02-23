# -*- coding:utf-8 -*-
# Author: Koctr


import xlrd
import xlwt
from xlutils.copy import copy


excel = xlrd.open_workbook("D:/7月下旬入库表.xlsx")
sheet = excel.sheet_by_index(0)

for row in range(0,sheet.nrows):


new_excel=copy(excel)
new_sheet=new_excel.add_sheet()

