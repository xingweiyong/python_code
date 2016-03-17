#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import chardet

request=urllib2.Request('http://www2.tjfdc.gov.cn/Lists/List51/DispForm1.aspx?ID=3')
response=urllib2.urlopen(request)
soup=BeautifulSoup(response)
#print soup.prettify()#beautifulsoup 默认把网页源码转成Unicode 再转成utf-8输出

temp=[]
for tag in soup.find_all('td'):
    if tag.has_attr('class') and tag.get('class')[0]=='UserArticleHeader':
        tit=tag.string+' '
        #temp.append(tit)

for tag in soup.find_all('tr'):
    if tag.has_attr('style') and tag['style']=='height:14.25pt':
        temp.append(tit)
        zone=tag.p.span.string
        if zone!=None:
            zone+=' '
        else:
            zone=u'蓟县'+' '
        temp.append(zone)
        if len(tag.select('span[lang="EN-US"]')) > 11:
            for i in range(1,12):#设置步长值可提高效率
                tag_temp=tag.select('span[lang="EN-US"]')[i].string
                if tag_temp!=None:
                    temp.append(tag_temp+' ')
                else:
                    continue
        temp.append('\r\n')
del temp[1]
for item in temp:
    #result_str+=repr(item)
    print item
def save_as(str,f):
    f.write(str)
result_f=file('result1.txt','a')
for item in temp:
    if item!=None:
        save_as(item.encode('utf-8'), result_f)
    else:
        continue
result_f.close()

