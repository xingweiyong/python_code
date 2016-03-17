def get_web(web_url):
    request=urllib2.Request(web_url)
    response=urllib2.urlopen(request)
    soup=BeautifulSoup(response)
    #print soup.prettify()#beautifulsoup 默认把网页源码转成Unicode 再转成utf-8输出
    temp=[]
    for tag in soup.find_all('td'):
        if tag.has_attr('class') and tag.get('class')[0]=='UserArticleHeader':
            tit=tag.string+' '
            temp.append(tit)
    for tag in soup.find_all('tr'):
        if tag.has_attr('style') and (tag['style'].find('height:')!=-1):
            if tag.p != None:
                print tag.p.span.string.encode('utf-8')
    for item in temp:
        print item
if __name__=='__main__':
    for i in [2,2000,3000]:
        url='http://www2.tjfdc.gov.cn/Lists/List51/DispForm1.aspx?ID='+ str(i)
        get_web(url)
