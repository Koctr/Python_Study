# -*- coding:utf-8 -*-
# Author: Koctr


import xlrd
import xlwt
from xlutils.copy import copy

excel = xlrd.open_workbook("D:/日统计.xls", formatting_info=True)
sheet = excel.sheet_by_index(0)

tmp_excel = copy(excel)
tmp_sheet = tmp_excel.get_sheet(0)

style1 = xlwt.XFStyle()

lishu_font = xlwt.Font()
lishu_font.name = "隶书"
lishu_font.bold = True
lishu_font.height = 18 * 20
style1.font = lishu_font

border = xlwt.Borders()
border.top = xlwt.Borders.THIN
border.bottom = xlwt.Borders.THIN
border.left = xlwt.Borders.THIN
border.right = xlwt.Borders.THIN
style1.borders = border

alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER
alignment.vert = xlwt.Alignment.VERT_CENTER
style1.alignment = alignment

style2 = xlwt.XFStyle()

song_font = xlwt.Font()
song_font.name = "宋体"
song_font.colour_index = 2
song_font.bold = True
song_font.height = 18 * 20
style2.font = song_font

style2.borders = border

num_alignment = xlwt.Alignment()
num_alignment.horz = xlwt.Alignment.HORZ_LEFT
num_alignment.vert = xlwt.Alignment.VERT_TOP
style2.alignment = num_alignment

style3 = xlwt.XFStyle()
song_font2 = xlwt.Font()
song_font2.name = "宋体"
song_font2.colour_index = 0
song_font2.bold = True
song_font2.height = 18 * 20
style3.font = song_font2

style3.borders = border
style3.alignment = num_alignment

top_cell_style = xlwt.XFStyle()
top_cell_style.font = lishu_font
top_cell_style.alignment = alignment

numbers = [3, 12, 15, 9]
index = 0
for row in range(0, sheet.nrows):
    for col in range(0, sheet.ncols):
        if (col == 1 and row == 0) or (col == 0 and row == 0):
            # (0, 0)和(0, 1)单元格不加边框
            tmp_sheet.write(row, col, sheet.row(row)[col].value, top_cell_style)
            continue
        elif not sheet.cell_value(row, col):
            if numbers[index] > 10:
                tmp_sheet.write(row, col, numbers[index], style2)
            else:
                tmp_sheet.write(row, col, numbers[index], style3)
            index += 1
            continue
        tmp_sheet.write(row, col, sheet.cell(row, col).value, style1)

tmp_excel.save("D:/日统计.xls")
