#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import chardet

request=urllib2.Request('http://www2.tjfdc.gov.cn/Lists/List51/DispForm1.aspx?ID=2')
response=urllib2.urlopen(request)
soup=BeautifulSoup(response)
#print soup.prettify()#beautifulsoup 默认把网页源码转成Unicode 再转成utf-8输出

temp=[]

for tag in soup.find_all('td'):
    if tag.has_attr('class') and tag.get('class')[0]=='UserArticleHeader':
        tit=tag.string
        temp.append(tit)

for tag in soup.find_all('tr'):
    if tag.has_attr('style') and tag['style']=='height:14.25pt':
        zone=tag.p.span.string
        temp.append(zone)
        if len(tag.select('span[lang="EN-US"]')) > 11:
            for i in range(1,12,2):
            #print len(tag.select('span[lang="EN-US"]'))
                temp.append(tag.select('span[lang="EN-US"]')[i].string)
                #print i
        else:
            continue
        temp.append(' ')
result_str=''
del temp[1]
for item in temp:
    result_str+=repr(item)
    #print item
print chardet.detect(result_str)
f=file('result1.txt','w')
#f.write(str(result_str.encode('utf-8')))
f.write(result_str.encode('utf-8','ignore'))
f.close()
#print chardet.detect(result_str.decode('ascii').encode('utf-8'))
#print chardet.detect(result_str)


'''
def save_as(atr,f):
    f.write(str)
f=file('result1.txt','a')
for item in temp:
    item=unicode(item)
    #print type(item)
    save_as(item,f)
f.close()
'''
