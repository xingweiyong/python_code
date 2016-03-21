#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#获取字段函数
def get_sub(str):
    num2=int(str.find('<',2))
    num1=int(str.find('">'))
    return str[num1+2:num2]
#保存文件函数
def save_as(str,f):
    f.write(str)
#检测网络连接异常
def check_error(web_url):
        try:
            request=urllib2.Request(web_url)
            response=urllib2.urlopen(request)
            soup=BeautifulSoup(response)
            return True
        except Exception,e:
            print e
            return False
#主体函数
def get_web(web_url):
    request=urllib2.Request(web_url)
    response=urllib2.urlopen(request)
    soup=BeautifulSoup(response)
    #print soup.prettify()#beautifulsoup 默认把网页源码转成Unicode 再转成utf-8输出
    temp=[]
    for tag in soup.find_all('td'):
        if tag.has_attr('class') and tag.get('class')[0]=='UserArticleHeader':
            tit=tag.string+' '
    for tag in soup.find_all('tr'):
        if tag.has_attr('style'):
            if tag['style']=='height:14.25pt':
                temp.append(tit)
                if tag.td.p.span.span!=None:
                    for i in tag.td.p.span.span.stripped_strings:
                        if i !=u'县':
                            #print i
                            temp.append(i+' ')
                else:
                    for item in tag.td.p.strings:
                        if item!=u'成交套数（套）':
                            #print item
                            temp.append(item+' ')
                item=tag.select('span[lang="EN-US"]')
                num_item=len(item)
                #print num_item
                if num_item >6: #过滤杂质
                    for i in range(0,num_item):
                        if item[i].string != None:
                            if item[i].string !=u'(':
                                temp.append(item[i].string+' ')
                    temp.append('\n')
            if tag['style']=='height:15.75pt':#网页样式改变
                temp.append(tit)
                if tag.td.p.span.font!=None:
                    #print get_sub(str(tag.td.p.span.font))
                    temp.append(get_sub(str(tag.td.p.span.font))+' ')
                    item=tag.select('span[lang="EN-US"]')
                    num_item1=len(item)
                    #print num_item1
                    if num_item1>11:
                        for i in range(0,num_item1):
                            if item[i].string!=None:
                                temp.append(item[i].string+' ')
                        temp.append('\n')
                else:
                    #print get_sub(str(tag.td.p.span))
                    temp.append(get_sub(str(tag.td.p.span))+' ')
                    item=tag.select('span[lang="EN-US"]')
                    num_item1=len(item)
                    if num_item1>11:
                        for i in range(0,num_item1):
                            if item[i].string!=None:
                                temp.append(item[i].string+' ')
                        temp.append('\n')
    try:
        result_f=file('result3.txt','a')
        if len(temp)!=0:
            if temp[1]==tit:
                del temp[0]
            if temp[1]==u'(':
                del temp[0:2]
        for item in temp:
            if item==u'蓟 ':
                item=u'蓟县'
            save_as(item.encode('utf-8'), result_f)
    finally:
        result_f.close()
if __name__=='__main__':
    for i in range(2,3079):#[3,1000,2000,3000,3015]
        url='http://www2.tjfdc.gov.cn/Lists/List51/DispForm1.aspx?ID='+ str(i)
        print url
        if check_error(url):
            get_web(url)
        else:
            continue
