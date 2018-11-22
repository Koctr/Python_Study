# -*- encoding:utf-8 -*-
# Author: Koctr


menu_file = open("menu", "r", encoding="utf-8")
menus = eval(menu_file.read())
menu_file.close()

is_exit = ""
current_layer = menus
layer=[]
while is_exit != "q":
    for k in current_layer:
        print(k)
    choice = input("请输入菜单名称进入下一级菜单，输入b返回上一级菜单，输入q退出程序：")
    if choice == "b":
        if not layer:
            print("没有上一级菜单")
        else:
            current_layer = layer[-1]
            layer.pop()
    elif choice == "q":
        is_exit = choice
    elif choice not in current_layer:
        print("无效的输入")
    else:
        layer.append(current_layer)
        current_layer = current_layer[choice]
        if not current_layer:
            print("没有下一级菜单")
            current_layer = layer[-1]
            layer.pop()