# -*- encoding:utf-8 -*-
# Author: Koctr


from core.service import admin_service, teacher_servcie, student_service


def print_main_menu():
    """
    打印主菜单
    :return: 无
    """
    menu = """
               ------主菜单------
               1. 管理入口
               2. 讲师入口
               3. 学生入口
               4. 退出
               """
    menu_dic = {
        "1": admin_service.login,
        "2": teacher_servcie.login,
        "3": student_service.login,
        "4": logout,
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input("请输入数字选择菜单：").strip()
        if user_option in menu_dic:
            menu_dic[user_option]()
        else:
            print("\33[31;1m无效的选择\33[0m")


def logout():
    """
    退出程序
    :return: 
    """
    print("再见")
    exit()
