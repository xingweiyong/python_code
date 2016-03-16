#coding:utf-8
import urllib2
from bs4 import BeautifulSoup

request=urllib2.Request('http://www2.tjfdc.gov.cn/Lists/List51/DispForm1.aspx?ID=2')
response=urllib2.urlopen(request)
soup=BeautifulSoup(response)
#print soup.prettify()#beautifulsoup 默认把网页源码转成Unicode 再转成utf-8输出

for tag in soup.find_all('td'):
    if tag.has_attr('class') and tag.get('class')[0]=='UserArticleHeader':
        print tag.string
