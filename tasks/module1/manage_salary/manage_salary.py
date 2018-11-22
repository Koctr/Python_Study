# -*- encoding:utf-8 -*-
# Author: Koctr

employees_data = {}
with open("info", "r", encoding="utf-8") as info:
    for line in info:
        employee_data = line.split()
        employees_data[employee_data[0]] = int(employee_data[1])

menu_list = ["查询员工工资", "修改员工工资", "增加新员工记录", "退出"]
exit_flag = False
while not exit_flag:
    for index, value in enumerate(menu_list):
        print("%s. " % (index + 1), value)
    choice = input(">>: ")
    if not choice.isdigit() or int(choice) <= 0 or int(choice) > 4:
        print("没有此菜单")
    else:
        choice = int(choice)
        user_input = ""
        employee_exist = False
        if choice == 1:
            user_input = input("请输入要查询的员工姓名（例如：Alex）：")
            if user_input in employees_data:
                print("%s的工资是：%d" % (user_input, employees_data[user_input]))
            else:
                print("您查询的员工不存在")
        elif choice == 2:
            user_input = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：")
            user_input = user_input.split()
            if len(user_input) == 2 and user_input[1].isdigit() and int(user_input[1]) > 0:
                if user_input[0] in employees_data:
                    employees_data[user_input[0]] = int(user_input[1])
                    print("修改成功")
                    employee_exist = True
                if not employee_exist:
                    print("要修改的员工不存在")
            else:
                print("您输入的格式不正确，或工资不是正整数")
        elif choice == 3:
            user_input = input("请输入要增加的员工姓名和工资，共空格分割（例如：Eric 100000）：")
            user_input = user_input.split()
            if len(user_input) == 2 and user_input[1].isdigit() and int(user_input[1]) > 0:
                if user_input[0] in employees_data:
                    print("要添加的员工已存在")
                    employee_exist = True
                if not employee_exist:
                    employees_data[user_input[0]] = int(user_input[1])
                    print("新增成功")
            else:
                print("您输入的格式不正确，或工资不是正整数")
        else:
            print("再见！")
            exit_flag = True

with open("info", "w", encoding="utf-8") as info:
    for employee_key in employees_data:
        info.writelines("%s %d\n" % (employee_key, employees_data[employee_key]))
