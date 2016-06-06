#coding:utf-8
import urllib
import urllib2
import cookielib
import re
from bs4 import BeautifulSoup
import block_list
import time,sys,datetime,random

#登录并保存cookie
post_url = 'http://ourob.cn/bbs/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'
url = 'http://ourob.cn/bbs/forum.php'
#url = 'http://ourob.cn/bbs/forum.php?mod=viewthread&tid=10075043'

'''
url = 'http://ourob.cn/bbs/forum.php?mod=viewthread&tid=10075043'
req = urllib2.Request(url)
res = urllib2.urlopen(req)
print res.read()
'''
err_str = '' #保存error详情
filename = 'cookie_ob.txt'
#请求报头
myheader =({
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Host':'ourob.cn',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection':'keep-alive'
})

cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#post请求参数
postdata = urllib.urlencode({
        'fastloginfield':'username',
        'handlekey':'ls',
        'username':'xingweiyong',
        'password':'19910629a',
        'quickforward':'yes',
        'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:46.0) Gecko/20100101 Firefox/46.0',
        'Connection':'keep-alive'
})
login_url = post_url
opener.open(login_url,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
try:
        result = opener.open(url)
except Exception,e:
        err_str += 'first page err:%s \n' %(e)
#time.sleep(random.randint(0,1))
str_0 = result.read() #str_0 列表页源码 
#print '源码长度：%d' %len(str_0)
#正则获取列表页 user_num,topic_num,online_num
user_num = 0
topic_num = 0
online_num = 0
pattern_topic_num = re.compile('<p class="chart z">今日: <em>(\d*?)</em><span class=')
topic_num = re.findall(pattern_topic_num,str_0)[0]
pattern_user_num = re.compile('</span>会员: <em>(\d*?)</em>')
user_num = re.findall(pattern_user_num,str_0)[0]
pattern_online_num = re.compile('<span class=.*?<strong>(\d*?)</strong>')
online_num = re.findall(pattern_online_num,str_0)[0]
result_0 = 'date:%s,今日发帖：%s,会员人数:%s,在线人数:%s,'%(time.ctime(time.time()),topic_num,user_num,online_num)
#补全链接函数
def full_url(list):
        for i,item in enumerate(list):
                list[i] = ('http://ourob.cn/bbs/' + item.replace('amp;',''))
        return list
#板块下爬虫
block_url = []
block_url = block_list.block_url
#增加翻页功能：简单起见，只翻2页
for i in range(31):
        list_temp = []
        list_temp.append(block_url[i][0] + '&page=2')
        list_temp.append(block_url[i][1])
        block_url.append(list_temp)

#print len(block_url)
for i in range(0,62):#range(len(block_url)):
        print 'num:%d,block_name:%s,blcok_url:%s'%(i,block_url[i][1],block_url[i][0])
        #print block_url[i][0],block_url[i][1]
        str_1 = '' #临时存储板块源码，用于后续提取正文url
        list_1 = [] #临时存储列表页中当日帖子的正文url
        try:
                cookie = cookielib.MozillaCookieJar()
                cookie.load('cookie_ob.txt',ignore_discard=True,ignore_expires=True)
                opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
                opener.open(login_url,postdata)
                str_1 = opener.open(block_url[i][0]).read()
        except Exception,e:
                err_str += 'block url:%s err:%s ' %(block_url[i][0],e)
        import time
        #time.sleep(random.randint(9,10))
        '''
        list_1 = str_1.split('em><span class="xi1">\.\*\?</span></em>')
        print len(list_1)
        '''
        if str_1 != '':
                soup = BeautifulSoup(str_1)
                #print soup.prettify()
                for tag in soup.find_all('td'):
                        if tag.em != None:
                                if tag.em.span != None:
                                        if tag.em.span.has_attr('class') and tag.em.span.get('class')[0] == 'xi1':
                                                #print tag.em.span.string
                                                #if tag.previous_sibling.previous_sibling.a.has_attr('class'):
                                                list_1 = re.findall(re.compile('href="(.*?)"'),str(tag.previous_sibling.previous_sibling.find_all('a',class_='xst')))
                                                #调用函数，自动补全list中url
                                                list_1 = full_url(list_1)
                                                #进行下一层爬虫-正文页
                                                for item in list_1:
                                                        str_2 = '' #临时存储正文页源码，供后续提取字段
                                                        str_3 = '' #临时存储楼主主页源码，供提取相关字段
                                                        name='';time='';view_num='';comment_num='';title = ''
                                                        #print item
                                                        try:
                                                                str_2 = opener.open(item).read()
                                                        except Exception,e:
                                                                err_str += 'content url:%s err:%s       ' %(item,e)
                                                        import time
                                                        #time.sleep(random.randint(0,1))
                                                        if str_2 != '':
                                                                name = re.findall(re.compile('<div class="authi"><a href=.*? target="_blank" class="xw1">(.*?)</a>'),str_2)[0]#list第一个元素表示楼主
                                                                time = re.findall(re.compile('>发表于 (.*?)</em>'),str_2)[0] #一定会有发帖时间，
且第一个是楼主
                                                                view_num = re.findall(re.compile('查看:</span> <span class="xi1">(.*?)</span>'),str_2)[0]
                                                                comment_num = re.findall(re.compile('回复:</span> <span class="xi1">(.*?)</span>'),str_2)[0]
                                                                title = re.findall(re.compile('id="thread_subject">(.*?)</a>'),str_2)[0]
                                                                result_2 = 'block:%s,name:%s,time:%s,view_num:%s,comment_num:%s,title:%s,' %(block_url[i][1],name,time,view_num,comment_num,title)
 try:
                                                                        str_3 = opener.open('http://ourob.cn/bbs/' + re.findall(re.compile('<div class="authi"><a href="(.*?)" target='),str_2)[0].replace('amp;','')).read()
                                                                except Exception,e:
                                                                        err_str += 'user url:%s err:%s\n' %(('http://ourob.cn/bbs/' + re.findall(re.compile('<div class="authi"><a href="(.*?)" target='),str_2)[0].replace('amp;','')),e)
                                                                import time
                                                                #time.sleep(random.randint(0,1))
                                                                if str_3 != '':
                                                                        sex='';bir='';blood_type='';jifen='';renpin='';ob='';ziyuan='';friends='';topics=''
                                                                        sex_temp = re.findall(re.compile('<li><em>性别</em>(.*?)</li>'),str_3)
                                                                        if len(sex) > 0:
                                                                                sex = sex_temp[0]
                                                                        else:
                                                                                sex = 'forbidden'
                                                                        bir_temp = re.findall(re.compile('<li><em>生日</em>(.*?)</li>'),str_3)
                                                                        if len(bir_temp) > 0:
                                                                                bir = bir_temp[0]
                                                                        else:
                                                                                bir = 'unknown'
                                                                        blood_type_temp = re.findall(re.compile('<li><em>血型</em>(.*?)</li>'),str_3)
                                                                        if len(blood_type_temp) > 0:
                                                                                blood_type = blood_type_temp[0]
                                                                        else:
                                                                                blood_type = 'unknown'
                                                                        jifen_temp = re.findall(re.compile('<li>积分: <a href=.*?>(.*?)</a></li>'),str_3)
                                                                        if len(jifen_temp) > 0:
                                                                                jifen = jifen_temp[0]
                                                                        else:
                                                                                jifen = 'forbidden'
                                                                        renpin_temp = re.findall(re.compile('<li>人品: <a href=.*?>(.*?)</a><li>'),str_3)
                                                                        if len(renpin_temp) > 0:
                                                                                renpin = renpin_temp[0]
else:
                                                                                renpin = 'forbidden'
                                                                        ob_temp = re.findall(re.compile('<li>OB: <a href=.*?>(.*?)</a>'),str_3)
                                                                        if len(ob_temp) > 0:
                                                                                ob = ob_temp[0]
                                                                        else:
                                                                                ob = 'forbidden'
                                                                        ziyuan_temp = re.findall(re.compile('<li>资源: <a href=.*?>(.*?)</a>'),str_3)
                                                                        if len(ziyuan_temp) > 0:
                                                                                ziyuan = ziyuan_temp[0]
                                                                        else:
                                                                                ziyuan = 'forbidden'
                                                                        friends_temp = re.findall(re.compile('<li>好友: <a href=.*?>(.*?)</a></li>'),str_3)
                                                                        if len(friends) > 0:
                                                                                friends = friends_temp[0]
                                                                        else:
                                                                                friends = 'forbidden'
                                                                        topics_temp = re.findall(re.compile('<li>主题: <a href=.*?>(.*?)</a></li>'),str_3)
                                                                        if len(topics_temp) > 0:
                                                                                topics = topics_temp[0]
                                                                        else:
                                                                                topics = 'forbidden'
                                                                        result_3 = 'sex:%s,bir:%s,blood_type:%s,jifen:%s,renpin:%s,ob:%s,ziyuan:%s,friends:%s,topics:%s \n' %(sex,bir,blood_type,jifen,renpin,ob,ziyuan,friends,topics)
                                                                        #写入文件
                                                                        try:
                                                                                with file('/home/xwy/文档/python/result_count.txt','a') as f:
                                                                                        f.write(result_0 + result_2 + result_3)
                                                                                if err_str != '':
                                                                                        with file('/home/xwy/文档/python/err_log.txt','a') as f:
                                                                                                f.write(err_str)
                                                                        except Exception,e:
                                                                                print e
                                                                        #print result_0 + result_2 + result_3
