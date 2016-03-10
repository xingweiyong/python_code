#查看内存
import psutil
>>> mem=psutil.virtual_memory()
>>> mem.total
4148744192L
>>> mem.used
1841168384L
#显示浮点型
from __future__ import division
#显示内存
psutil.cpu.times()
psutil.cpu_count()
psutil.cpu.count(logical=False
#查看磁盘信息
psutil.disk_partitions()
psutil.disk_usages('/')#磁盘分区的使用情况
psutil.disk_io_counters()#获得磁盘总的IO个数
psitil.disk_io_counters(perdisk=True)#获取单个分区的io个数
#查看网络信息
psutil.net_io_counters()
psutil.net_io_counters(pernic=True)#查看一个端口的网络信息
#查看其他信息
psutil.users()#获取登录系统的用户信息
import datetime
datetime.datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
#查看DNS MX 记录
import dns.resolver
domain=raw_input('please input an domain: ')
MX=dns.resolver.query(domain,'MX')
for i in MX:
    print 'MX preference =',i.preference,'main exchanger=',i.exchange
#查看NS记录、其余类似
import dns.resolver
domain=raw_input('please input an domain: ')
ns=dns.resolver.query(domain,'NS')
for i in ns.response.answer:
    for j in i.items:
        print j.to_text()
#查看DNS A 记录
import dns.resolver
domain=raw_input('please input an domain: ')
A=dns.resolver.query(domain,'A')
for i in A.response.answer:
    for j in i.items:
        print j.address

#dns解析、轮循监控
import dns.resolver
import os
import httplib

iplist=[]
appdomain='www.hylanda.com'

def get_iplist(domain=''):
    try:
        A=dns.resolver.query(domain,'A')
    except Exception,e:
        print 'dns resolver error: '+str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl=ip+':80'
    getcontent=''
    httplib.socket.setdefaulttimeout(5)
    conn=httplib.HTTPConnection(checkurl)

    try:
        conn.request('GET','/',headers={'Host':appdomain})

        r=conn.getresponse()
        getcontent=r.read()
        #print len(getcontent)
    finally:
        if len(getcontent)>10000:

            print ip+'[ok]'
        else:
            print ip+'[error]'
if __name__=='__main__':
    if get_iplist(appdomain) and len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print 'dns resolver error'
#求列表中频数
mylist = [2,2,2,2,2,2,3,3,3,3]
myset = set(mylist)#build an unordered collection of unique elements

for item in myset:
    print mylist.count(item), " of ", item, " in list" #return the frequence of the item

