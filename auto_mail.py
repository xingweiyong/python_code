#coding:utf-8
import smtplib
import string

HOST='smtp.qq.com'
SUBJECT='test email from python'
TO='1531694185@qq.com'
FROM='441078355@qq.com'
text='python rules the all'
BODY=string.join((
    'From: %s' %FROM,
    'To: %s' %TO,
    'Subject: %s' %SUBJECT,
    '',
    text
    ),'\r\n')
server=smtplib.SMTP()
server.connect(HOST,'25')
server.starttls()
server.login('441078355@qq.com','bedmayrwrohfbhbe')#发送邮箱需开通 smtp服务设置
server.sendmail(FROM,TO,BODY)
server.quit()
