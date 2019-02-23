# -*- coding:utf-8 -*-
# Author: Koctr


import xlrd
import xlwt
from xlutils.copy import copy

excel = xlrd.open_workbook("D:/7月下旬入库表.xlsx")
sheet = excel.sheet_by_index(0)

all_data = []
for row in range(1, sheet.nrows):
    company = sheet.cell(row, 1).value
    price = sheet.row(row)[3].value
    weight = sheet.cell_value(row, 4)
    data = {"company": company, "price": price, "weight": weight}
    all_data.append(data)

weights = [[], [], [], []]
total_prices = [[], [], [], []]

for data in all_data:
    if data['company'] == "张三粮配":
        weights[0].append(data["weight"])
        total_prices[0].append(data["price"] * data["weight"])
    if data['company'] == '李四粮食':
        weights[1].append(data['weight'])
        total_prices[1].append(data['weight'] * data['price'])
    if data['company'] == '王五小麦':
        weights[2].append(data['weight'])
        total_prices[2].append(data['weight'] * data['price'])
    if data['company'] == '赵六麦子专营':
        weights[3].append(data['weight'])
        total_prices[3].append(data['weight'] * data['price'])

tmp_excel = xlrd.open_workbook("D:/7月下旬统计表.xls", formatting_info=True)

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

new_sheet.write(2, 1, len(weights[0]), style)
new_sheet.write(2, 2, round(sum(weights[0]), 2), style)
new_sheet.write(2, 3, round(sum(total_prices[0]), 2), style)
new_sheet.write(3, 1, len(weights[1]), style)
new_sheet.write(3, 2, round(sum(weights[1]), 2), style)
new_sheet.write(3, 3, round(sum(total_prices[1]), 2), style)
new_sheet.write(4, 1, len(weights[2]), style)
new_sheet.write(4, 2, round(sum(weights[2]), 2), style)
new_sheet.write(4, 3, round(sum(total_prices[2]), 2), style)
new_sheet.write(5, 1, len(weights[3]), style)
new_sheet.write(5, 2, round(sum(weights[3]), 2), style)
new_sheet.write(5, 3, round(sum(total_prices[3]), 2), style)

new_excel.save('D:/7月下旬统计表.xls')
