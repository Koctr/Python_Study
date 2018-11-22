# -*- encoding:utf-8 -*-
# Author: Koctr


import os

# 商品列表，从products文件中读取
product_list = []
with open("products", "r", encoding="utf-8") as products_file:
    for line in products_file:
        product = line.split(", ")
        product[1] = int(product[1])
        product_list.append(product)

username = input("请输入用户名：")
password = input("请输入密码：")

with open("users_data", "r", encoding="utf-8") as users_data, \
        open("users_data.bak", "w", encoding="utf-8") as users_data_bak:
    # 标示用户是否第一次登录
    user_exist = False
    # 用户数据
    user_data = {}
    # 一行一行读取users_data文件，写入users_data.bak
    for line in users_data:
        if username in eval(line):
            # 如果用户在users_data中存在，不写入users_data.bak，待用户退出时再写入，并且设置user_data
            user_data = eval(line)
            user_exist = True
            print('您的用户余额是\033[32;1m%s\033[0m' % user_data[username]["balance"])
        else:
            users_data_bak.writelines(line)
    if not user_exist:
        salary = ""
        # 标示工资输入是否符合要求的变量
        saraly_check = False
        while not saraly_check:
            salary = input("请输入您的工资：")
            if not salary.isdigit() or int(salary) <= 0:
                print("请输入大于0的整数工资")
            else:
                salary = int(salary)
                print("您的\033[32;1m工资是%s\033[0m" % salary)
                saraly_check = True
        user_data[username] = {"items": [], "balance": int(salary)}
    # 标示是否退出的变量
    exit_flag = False
    # 用户本次登录后已购商品列表
    item_list = []
    while not exit_flag:
        print("商品列表：")
        for index, value in enumerate(product_list):
            print(index, value)
        choice = input("输入商品编号购买商品，输入f查询购买记录，输入q退出程序：")
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice < len(product_list):
                if user_data[username]["balance"] >= product_list[choice][1]:
                    user_data[username]["balance"] -= product_list[choice][1]
                    item_list.append(product_list[choice])
                    print("所选商品\033[32;1m%s已加入购物车\033[0m，" % product_list[choice])
                    print("您的\033[32;1m余额是%s\033[0m" % user_data[username]["balance"])
                else:
                    print("您的余额不足，\033[31;1m余额是%s\033[0m" % user_data[username]["balance"])
            else:
                print("编号标示的\033[31;1m商品不存在\033[0m，请重新输入")
                print("您的\033[32;1m余额是%s\033[0m" % user_data[username]["balance"])
        else:
            if choice == 'f':
                print("您的消费记录如下：")
                for v in user_data[username]["items"]:
                    print(v)
                for v in item_list:
                    print(v)
            elif choice == 'q':
                exit_flag = True
                user_data[username]["items"].extend(item_list)
                print("您购买的商品如下：")
                for i, v in enumerate(item_list):
                    print(i, v)
                print("您的\033[32;1m余额是%s\033[0m" % user_data[username]["balance"])
            else:
                print('\033[31;1m无效的输入\033[0m')
                print("您的\033[32;1m余额是%s\033[0m" % user_data[username]["balance"])
    users_data_bak.writelines(str(user_data)+"\n")
os.remove("users_data")
os.rename("users_data.bak", "users_data")
