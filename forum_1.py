#coding:utf-8
import urllib2
import urllib
import re
import time
import sys

pattern_str1=sys.argv[1]#正则表达式中引号需\转义，双引号括起
num=int(sys.argv[2])#传参 正则表达式中返回值得个数
page=int(sys.argv[3])#传参 翻页
pattern_str='<dt><span class=""></span>[^<>]*?<a[^<>]*?target="_blank" href="(.*?)">[^<>]*?(.*?)</a>'
result3=''#保存规则不能匹配的URL
print pattern_str
#伪装报头
req_headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
         'Accept':'image/png,image/*;q=0.8,*/*;q=0.5',
         'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
         'Connection':'keep-alive'}

def get_content(url):
    request=urllib2.Request(url,data = None,headers = req_headers)
    response=urllib2.urlopen(request)
    web_get=response.read()
    result=''#储存返回结果
    #print len(web_get),type(web_get)

    pattern=re.compile(pattern_str)
    if re.findall(pattern,web_get):
        for item in re.findall(pattern,web_get):
            for i in range(0,num):
                if i !=num-1:
                    result+=item[i]+'$'#分割标题和url
                else:
                    result+=item[i]+'\n'
        f=file('E:\webcam\ss.txt','a')
        f.write(result)
        f.close()
    else:
        global result3
        result3+=url+'\n'
    #print result

for i in range(0,page):
    url='http://club.autohome.com.cn/bbs/forum-c-266-%d.html?qaType=-1#pvareaid=101061'%i
    get_content(url)
    print i
if result3!='':
    f=file('auto_failed1.txt','w')
    f.write(result3)
    f.close()
