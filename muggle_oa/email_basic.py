# -*-coding:utf-8-*-
# Author: "Koctr"


import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

smtp_server = "smtp.sina.com"
sender_email = "pythonauto@sina.com"
sender_email_pwd = "python1234"
receiver_emails_and_calls = (("pythonauto@sina.com", "Koctr"), ("koctr_2004@163.com", "Alex"))

for address_and_call in receiver_emails_and_calls:
    try:
        mail_content = "Hello, {__email}.这是一封测试邮件。".format(__email=address_and_call[1])
        mail_title = "Python办公自动化测试邮件"

        msg = MIMEMultipart()
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_email
        msg["To"] = Header('%s' % address_and_call[1], 'utf-8')

        msg.attach(MIMEText(mail_content, 'plain', 'utf-8'))

        smtp = SMTP_SSL(smtp_server)
        smtp.login(sender_email, sender_email_pwd)
        smtp.sendmail(sender_email, address_and_call[0], msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("向%s发送邮件失败" % address_and_call[0])
