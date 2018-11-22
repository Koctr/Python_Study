# -*- coding:utf-8 -*-
# Author: Koctr


# 新式类和经典类

class Person1(object):
    """新式类
    super(..., self).__init__(...)
    Python 2，多继承时广度查询
    """
    pass

class Person2:
    """经典类
    ParentClass.__init__(self, ...)
    Python 2，多继承时深度查询
    """
    pass


