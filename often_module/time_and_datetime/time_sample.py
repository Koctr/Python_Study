# -*- coding:utf-8 -*-
# Author: Koctr

import time

"""
时间表示法：
1. 字符串格式
2. 时间戳
3. tuple
"""

"""
1: 2 -> 1
"""
print(type(time.ctime(3320482710)), time.ctime(3320482710))

"""
1: 3 -> 1
"""
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(time.asctime(time.localtime(3928402785)))

"""
2: 3 -> 2
"""
print(time.mktime(time.localtime()))

"""
3: 1 -> 3
"""
print(time.strptime("2018-11-14 21:49:33", "%Y-%m-%d %H:%M:%S").tm_yday)

"""
3: 2 -> 3
"""
print(time.localtime(20484024))
print(time.gmtime(2048275405))

"""
属性
"""
print(time.timezone / 3600)
print(time.altzone)
print(time.daylight)
print("休眠3秒")
time.sleep(3)
