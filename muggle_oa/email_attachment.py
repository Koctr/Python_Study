# -*-coding:utf-8-*-
# Author: "Koctr"


import smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header

smtp_server = "smtp.sina.com"
sender = "pythonauto@sina.com"
pwd = "python1234"
info_list = (("pythonauto@sina.com", "Koctr", 'C:/000/表格样式.docx'),
             ("koctr_2004@163.com", "Alex", 'C:/000/paragraph.docx'))

for info in info_list:
    content = "Hello，%s。请查看附件。" % info[1]
    title = "带附件的邮件"

    msg = MIMEMultipart()
    msg["Subject"] = Header(title, 'utf-8')
    msg['From'] = sender
    msg['To'] = Header(info[1], 'utf-8')
    msg.attach(MIMEText(content, 'plain', 'utf-8'))

    attachment = MIMEApplication(open(info[2], 'rb').read())
    attachment.add_header('Content-Disposition', 'attachment', filename=Header(info[2].split("/")[-1],
                          'utf-8').encode())
    msg.attach(attachment)

    try:
        smtp = SMTP_SSL(smtp_server)
        smtp.set_debuglevel(0)
        smtp.ehlo(smtp_server)
        smtp.login(sender, pwd)

        smtp.sendmail(sender, info[0], msg.as_string())
        smtp.quit()
        print('邮件发送成功')
    except smtplib.SMTPException:
        print("邮件%s发送失败" % info[0])
