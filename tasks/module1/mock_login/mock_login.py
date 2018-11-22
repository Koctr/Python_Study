# -*- encoding:utf-8 -*-
# Author: Koctr

MAX_LOGIN_FAILURE_TIMES = 3
locked_users = []
with open("locked_users", "r", encoding="utf-8") as locked_file:
    for line in locked_file:
        locked_users.append(line.strip())

users_info = {}
with open("users_info", "r", encoding="utf-8") as users_info_file:
    for line in users_info_file:
        user_info = line.split()
        users_info[user_info[0]] = [user_info[1], int(user_info[2]), int(user_info[3])]

# 不存在的用户登录3次，退出
not_exist_user_login_time = 0

exit_flag = False
while True:
    username = input("请输入用户名：")
    password = input("请输入密码：")

    locked_user = False
    if username in locked_users:
        print("用户已被锁定，无法登录")
        users_info[username][2] += 1
        if users_info[username][2] >= MAX_LOGIN_FAILURE_TIMES:
            print("登录次数超限，程序退出")
            break
        locked_user = True

    if not locked_user:
        if username in users_info:
            if password == users_info[username][0]:
                print("恭喜你，登录成功")
                users_info[username][1] = 0
                break
            else:
                print("用户名或密码错误")
                users_info[username][1] += 1
                users_info[username][2] += 1
                if users_info[username][1] >= MAX_LOGIN_FAILURE_TIMES:
                    print("登录失败三次，用户被锁定")
                    locked_users.append(username)
                if users_info[username][2] >= MAX_LOGIN_FAILURE_TIMES:
                    print("登录次数超限，程序退出")
                    break
        else:
            print("用户不存在")
            not_exist_user_login_time += 1
            if not_exist_user_login_time >= MAX_LOGIN_FAILURE_TIMES:
                print("登录次数超限，程序退出")
                break
# 重新写文件时，登录次数全部重置为0
with open("users_info", "w", encoding="utf-8") as users_info_file:
    for key in users_info:
        # print(key)
        users_info_file.writelines("%s %s %d 0\n" %(key, users_info[key][0], users_info[key][1]))
with open("locked_users", "w", encoding="utf-8") as locked_file:
    for user in locked_users:
        locked_file.writelines("%s\n" % user)
