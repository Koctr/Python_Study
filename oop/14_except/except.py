# -*- coding:utf-8 -*-
# Author: Koctr

"""演示异常处理"""

data = dict()
names = ["1", "2", "3"]
try:
    names[3]
    data["name"]
except KeyError as e:
    print("没有这个key", e)
except IndexError as e:
    print("列表错误", e)

try:
    names[3]
    data["name"]
except (KeyError, IndexError) as e:
    print("存在错误", e)
except Exception as e:
    # 捕获其他异常
    print("出错了", e)
else:
    print("一切正常")
finally:
    print("不管是否出错都执行")

try:
    names[3]
    data["name"]
except Exception as e:
    print("出错了", e)
else:
    print("一切正常")
finally:
    print("不管是否出错都执行")
