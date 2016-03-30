#coding:utf-8
import urllib2
import urllib
import re
import time
import sys
from bs4 import BeautifulSoup
import chardet

result3=''#保存规则不能匹配的URL

#定义去除空列表元素的函数
def remove_null(li):
    while '' in li:
        li.remove('')
#定义获取网页指定内容函数
def get_content(url):
    request=urllib2.Request(url)
    response=urllib2.urlopen(request)
    soup=BeautifulSoup(response,from_encoding="gb18030")#指定网页编码方式
    result=''#保存网页正文title
    result1=''#保存对应title的url
    result2=''#用于拼接输出结果，标题+URL
    for tag in soup.find_all('dl'):
        if tag.get('class')[0]=='list_dl' and tag.dt.a != None:
            result += tag.a.string+'\n'
            result1 +=tag.dt.a.get('href')+'\n'
    title_list=result.split('\n')
    url_list=result1.split('\n')
    for i in range(0,len(title_list)):
        title_list[i]=title_list[i].strip()#去除标题文字多于空格

    remove_null(title_list)#去除空列表元素
    remove_null(url_list)
    if len(title_list)==len(url_list):
        for i in range(0,len(title_list)):
            if title_list[i] == u'全部帖子':#全部帖子可扩展为一个杂质池
                title_list[i]=''
                url_list[i]=''
        remove_null(title_list)
        remove_null(url_list)
        for i in range(0,len(title_list)):
            result2+=title_list[i]+'$'+'http://club.autohome.com.cn'+url_list[i]+'\n'
    else:
        result3+=url+'\n'
    f=file('url.txt','a')
    f.write(result2.encode('utf-8'))
    f.close()
for item in range(0,int(sys.argv[1])):
    url='http://club.autohome.com.cn/bbs/forum-c-2288-%d.html?qaType=-1#pvareaid=101061'%item
    print item
    get_content(url)
if result3!='':
    f=file('url1.txt','w')
    f.write(result3)
    f.close()
