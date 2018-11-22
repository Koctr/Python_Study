# -*- encoding:utf-8 -*-
# Author: Koctr


def check_login(login_type):
    """
    用于验证登录的装饰器
    :param login_type: 登录类型
    :return: 外层装饰器
    """
    def outer_wrapper(func):
        """
        外层装饰器
        :param func: 被装饰的函数
        :return: 内层装饰器
        """
        def wrapper(*args, **kwargs):
            """
            内层装饰器
            :param args: 可变元组参数
            :param kwargs: 可变字典参数
            :return: 被装饰函数运行结果
            """
            if user_data.get("authc"):
                res = func(*args, **kwargs)
                return res
            username = input("Input your username:").strip()
            password = input("Input your password:").strip()
            if login_type == "file":
                if username == "K0ctr" and password == "Koctr":
                    res = func(*args, **kwargs)
                    user_data["authc"] = True
                    return res
                else:
                    print("Invalid username or password.")
        return wrapper
    return outer_wrapper


user_data = {"authc": None}


@check_login("file")
def run1():
    print("In the run1")
    return 1


@check_login("file")
def run2(name):
    print("In the run2")
    return name

run1()
run = run2("tiantian")
print(run)
