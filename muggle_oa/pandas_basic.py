# -*- coding: utf-8 -*-
# author = 'K0ctr'

import pandas as pd

# 使用tuple建立dataframe
a_tuple = (1, 2, 3, 4, 5, 6)
df_for_tuple = pd.DataFrame(a_tuple)
print(df_for_tuple)

# 使用dict建立dataframe
a_dict = {
    'name': 'Koctr',
    'sex': '男',
    'age': '18'
}
df_for_dict = pd.DataFrame(a_dict,index=[0])
print(df_for_dict)

# 使用excel建立dataframe
dt_for_excel = pd.read_excel("D:/7月下旬统计表.xls")
df_for_excel = pd.DataFrame(dt_for_excel)
print(df_for_excel)
