# -*- coding:utf-8 -*-
# Author: Koctr

from datetime import datetime
from datetime import timedelta

print(datetime.now())
print(datetime.now() + timedelta(3))
print(datetime.now() + timedelta(hours=3))
print(datetime.now().replace(year=2016, minute=9))
