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
        mail_content = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html>
        <head>
            <meta charset="UTF-8">
            <title>测试邮件</title>
        </head>
        <body>
            Hello, {__email}。这是一封<a href="http://www.baidu.com">测试邮件</a>。
        </body>
        </html>
        """.format(__email=address_and_call[1])
        mail_title = "Python办公自动化测试邮件"

        msg = MIMEMultipart()
        msg["Subject"] = Header(mail_title, 'utf-8')
        msg["From"] = sender_email
        msg["To"] = Header('%s' % address_and_call[1], 'utf-8')

        msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

        smtp = SMTP_SSL(smtp_server)
        smtp.set_debuglevel(0)
        smtp.ehlo(smtp_server)
        smtp.login(sender_email, sender_email_pwd)
        smtp.sendmail(sender_email, address_and_call[0], msg.as_string())
        smtp.quit()
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("向%s发送邮件失败" % address_and_call[0])