# -*- coding: utf-8 -*-
# author = 'K0ctr'


import pandas as pd
import numpy as np

excel = pd.ExcelFile("D:/7月下旬入库表.xlsx")
data = excel.parse('7月下旬入库表')

pt1 = pd.pivot_table(data, index=['销售商'], columns=['来源省份'], values=['入库量（吨）'], aggfunc=np.sum, margins=True)
print(pt1)

pt2 = pd.pivot_table(data, index=['销售商'], columns=['来源省份'], values=['入库量（吨）'], aggfunc=np.size, margins=True)
print(pt2)

print("iat", pt1.iat[2, 1])
print("iloc", pt1.iloc[2, 1])
