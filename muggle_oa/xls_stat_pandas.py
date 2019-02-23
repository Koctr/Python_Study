# -*- coding: utf-8 -*-
__author__ = 'K0ctr'

import xlrd
import xlwt
import pandas
from xlutils.copy import copy

tmp_excel = xlrd.open_workbook("D:/7月下旬统计表.xls", formatting_info=True)
tmp_sheet = tmp_excel.sheet_by_index(0)

new_excel = copy(tmp_excel)
new_sheet = new_excel.get_sheet(0)

style = xlwt.XFStyle()

font = xlwt.Font()
font.name = "微软雅黑"
font.bold = True
font.height = 18 * 20
style.font = font

borders = xlwt.Borders()
borders.top = xlwt.Borders.THIN
borders.bottom = xlwt.Borders.THIN
borders.left = xlwt.Borders.THIN
borders.right = xlwt.Borders.THIN
style.borders = borders

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style.alignment = alignment

data = pandas.read_excel("D:/7月下旬入库表.xlsx")
weight = data["入库量（吨）"].groupby(data["销售商"], sort=True).sum()
total_price = (data["单价（元/吨）"] * data["入库量（吨）"]).groupby(data["销售商"], sort=True).sum()
amount = data["销售商"].groupby(data['销售商'], sort=True).count()

for key in weight.index:
    for row in range(2, tmp_sheet.nrows):
        if key == tmp_sheet.cell(row, 0).value:
            new_sheet.write(row, 1, int(amount.get(key)), style)
            new_sheet.write(row, 2, round(weight.get(key), 2), style)
            new_sheet.write(row, 3, round(total_price.get(key), 2), style)

new_excel.save("D:/7月下旬统计表.xls")
