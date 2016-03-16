#coding:utf-8
import smtplib
from email.mime.text import MIMEText

HOST='smtp.qq.com'
FROM='441078355@qq.com'
TO='1531694185@qq.com'
SUBJECT=u'官网流量数据报表'
msg=MIMEText('''
<table width="800" border="0" cellspacing="0" cellpadding="4">
  <tr>
    <td bgcolor="#cecfad" height="20" style=font-size:"4">*官网数据<a href="www.baidu.com">更多>></a></td>
  </tr>
  <tr>
    <td bgcolor="#efebde" height="100" style="font-size:13px">
      1) 日访问量：<font color="red">145652</font> 访问次数：23651 页面流量：5487 点击数：55589 数据流量：50M<br>
      2)状态码信息<br>
      &nbsp;&nbsp;123456789<br>
      3)访客浏览器信息<br>
      &nbsp;&nbsp;IE:50% firefox:20% chrome:10% other:20%<br>
      4)页面信息<br>
      &nbsp;&nbsp;/index.php 21548<br>
      &nbsp;&nbsp;/view.php 145698<br>
      &nbsp;&nbsp;/login.php 5469<br>
    </td>
  </tr>
</table>
''','html','utf-8')
msg['Subject']=SUBJECT
msg['From']=FROM
msg['To']=TO

try:
    server=smtplib.SMTP()
    server.connect(HOST,'25')
    server.starttls()
    server.login('441078355@qq.com','bedmayrwrohfbhbe')
    server.sendmail(FROM,TO,msg.as_string())#sendmail 发送的内容为string类型,body/msg,as_string()
    server.quit()
    print '邮件发送成功~'
except Exception,e:
    print '失败'+str(e)
