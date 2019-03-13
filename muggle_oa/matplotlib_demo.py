# -*- coding: utf-8 -*-
# author = 'K0ctr'


import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

date = ['2018/7/21', '2018/7/22', '2018/7/23', '2018/7/24', '2018/7/25', '2018/7/26', '2018/7/27', '2018/7/28',
        '2018/7/29', '2018/7/30', '2018/7/31']
hebei = [69, 93, 65, 65, 66, 70, 88, 47, 58, 21, 24]
shanxi = [36, 37, 41, 38, 36, 35, 57, 19, 32, 12, 21]

plt.plot(date, hebei, color="red", label="河北")
plt.plot(date, shanxi, color="blue", label="山西")

plt.title('每日入库量对比')
plt.xlabel('日期')
plt.ylabel('车次')

plt.legend()
plt.savefig("D:/stat.jpg")
plt.yticks(range(20, 100, 20))
plt.show()
