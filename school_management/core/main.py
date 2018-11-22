# -*- coding:utf-8 -*-
# Author: Koctr


from conf import settings
from core.clazz import School
from core.clazz import Course
from core.service import base_service
import configparser


"""
学校管理主程序
"""


def run():
    """
    学校管理程序入口
    :return: 
    """
    # Main.check_is_first_run()
    config = configparser.ConfigParser()
    config.read("%s/conf/init.ini" % settings.BASE_DIR, encoding="utf-8")
    if config["run"]["first_run"] == 'yes':
        s1 = School(None, "Beijing")
        s1.save()
        s2 = School(None, "Shanghai")
        s2.save()
        c1 = Course(None, 'Linux', 6000, 6)
        c2 = Course(None, 'Python', 8000, 12)
        c3 = Course(None, 'Go', 5000, 3)
        s1.create_course(c1)
        s1.create_course(c2)
        s2.create_course(c3)
        config.set("run", "first_run", 'no')
        config.write(open("%s/conf/init.ini" % settings.BASE_DIR, "w"))
    base_service.print_main_menu()
