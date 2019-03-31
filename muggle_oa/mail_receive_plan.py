# -*- encoding:utf-8 -*-
# Author: Koctr


import zmail
from tkinter import *
import tkinter.messagebox


server = zmail.server('koctr_2004@163.com','iyclnmdb123.')
mail = server.get_latest()

new_id = str(mail['id'])
print(new_id)

file_read = open('id.txt', 'r', encoding='utf-8')
old_id = file_read.readline()
file_read.close()

with open('id.txt', 'w', encoding='utf-8') as file_write:
	file_write.write(new_id)
	
if old_id != new_id:
	main_window = Tk()
	main_window.withdraw()
	tkinter.messagebox.showinfo('你有新邮件了', '邮件标题: %s' % mail['Subject'])

