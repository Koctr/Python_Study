# -*- coding: utf-8 -*-
# author = 'K0ctr'


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel = pd.ExcelFile("D:/7月下旬入库表.xlsx")
data = excel.parse('7月下旬入库表')
pt = pd.pivot_table(data, index=['销售商'], columns=['来源省份'], values=['入库量（吨）'], aggfunc=np.size, margins=True)

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

pt.plot()
pt.plot(kind='bar')
pt.plot(kind='area')

plt.xticks(rotation=0)
plt.title('各省入库量对比')
plt.xlabel('客户')
plt.ylabel('入库量')

plt.legend()
plt.show()
