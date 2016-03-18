#coding:utf-8
import urllib2
from bs4 import BeautifulSoup

def get_sub(str):
    num2=int(str.find('<',2))
    num1=int(str.find('">'))
    return str[num1+2:num2]
def save_as(str,f):
    f.write(str)

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
                if tag.td.p.span.string != None:
                    temp.append(tit)
                    zone=tag.td.p.span.string+" "
                    temp.append(zone)
                item=tag.select('span[lang="EN-US"]')
                num_item=len(item)
                if num_item >11:
                    for i in range(0,num_item):
                        if item[i].string != None:
                            temp.append(item[i].string+' ')
                    temp.append('\r\n')
            if tag['style']=='height:15.75pt':
                if tag.td.p.span.font!=None:
                    print get_sub(str(tag.td.p.span.font))
                else:
                    print get_sub(str(tag.td.p.span))
    for item in temp:
        print item
    try:
        result_f=file('result3.txt','a')
        for item in temp:
            save_as(item.encode('utf-8'), result_f)
    finally:
        result_f.close()
if __name__=='__main__':
    for i in [3,1000,2000]:#[3,1000,2000,3000,3015]
        url='http://www2.tjfdc.gov.cn/Lists/List51/DispForm1.aspx?ID='+ str(i)
        print url
        get_web(url)
