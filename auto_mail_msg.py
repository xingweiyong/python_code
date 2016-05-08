#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json
import random
import smtplib
import string
from email.mime.text import MIMEText


reload(sys)
sys.setdefaultencoding('utf-8')

page_num = random.randint(1,500)


#url = 'http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=%d'%page_num
url = 'http://api.1-blog.com/biz/bizserver/xiaohua/list.do?page=%d'%page_num
req = urllib2.Request(url)
#req.add_header("apikey", "a01d7c8e388313fe01009046a4857ea9")
resp = urllib2.urlopen(req)
content = resp.read()
if (content):
        print 'content ok'
        #print content
#解析json串

dic_str = json.loads(content)


num = random.randint(0,9)
#joke_title =  dic_str['showapi_res_body']['contentlist'][num]['title']
#joke_text =  dic_str['showapi_res_body']['contentlist'][num]['text']
joke_str = u'开心是一天，不开心也是一天，何不开开心心的呢？！' + '\n'*2 + u'**笑话**' +'\n'*2

for i in range(0,10):
        joke_str += 'title:' + dic_str['detail'][num + i]['author'] + '\n' + 'content:' + dic_str['detail'][num + i]['content'] + '\n' + '---'*20 + '\n'
        #joke_str += 'title:' + dic_str['showapi_res_body']['contentlist'][num + i]['title'] + '\n' + 'content:' + dic_str['showapi_res_body']['contentlist'][num + i]['text'] + '\n' + '---'*20 + '\n'
joke_str += u'来源：ITeye'
#发送电子邮件，普通文本格式
#print joke_str
HOST='smtp.163.com'
SUBJECT='happy new day~~~'
TO=['收信人列表']
FROM='*****@163.com'
text=joke_str
BODY=string.join((
    'From: %s' %FROM,
    'To: %s' %TO,
    'Subject: %s' %SUBJECT,
    '',
    text
    ),'\r\n')

try:
    server=smtplib.SMTP()
    server.connect(HOST,'25')
    server.starttls()
    server.login('****@163.com','password')
    for item in TO:
        server.sendmail(FROM,item,BODY)#sendmail 发送的内容为string类型,body/msg,as_string()
    server.quit()
    print '邮件发送成功~'
except Exception,e:
    print '失败'+str(e)
