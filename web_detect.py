    coding:utf-8
import sys,os
import time
import pycurl

URL = "http://www.baidu.com"
c = pycurl.Curl()
c.setopt(pycurl.URL,URL) #定义请求的url常量
c.setopt(pycurl.CONNECTTIMEOUT,5) #连接等待时间
c.setopt(pycurl.TIMEOUT,5) #请求等待时间
c.setopt(pycurl.NOPROGRESS,1) #0启用，非零屏蔽
c.setopt(pycurl.FORBID_REUSE,1) #完成交互后强制断开连接，不重用
c.setopt(pycurl.MAXREDIRS,1) #指向http重定向的最大数为1
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30) #设置保存dns信息的时间为30秒

indexfile = open(os.path.dirname(os.path.realpath(__file__)) + "/content.txt","wb")
c.setopt(pycurl.WRITEHEADER,indexfile)
c.setopt(pycurl.WRITEDATA,indexfile)

try:
        c.perform()
except Exception,e:
        print 'connection err:'+str(e)
        indexfile.close()
        c.close()
        sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME) #dns解析时间
CONNECT_TIME = c.getinfo(c.CONNECT_TIME) #获取建立连接的时间
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME) #获取从建立连接到准备传输消耗的时间
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME) #从...到传输开始消耗的时间
TOTAL_TIME = c.getinfo(c.TOTAL_TIME) #传输总时间
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD) #获取数据包大小
HEADER_SIZE = c.getinfo(c.HEADER_SIZE) #http头部大小
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD) #平均下载速度

print 'http状态码：%s'%HTTP_CODE
print 'dns解析时间：%.2f ms'%(NAMELOOKUP_TIME*1000)
print '建立连接时间：%.2f ms'%(CONNECT_TIME*1000)
print '准备传输时间：%.2f ms'%(PRETRANSFER_TIME*1000)
print '传输开始时间：%.2f ms'%(STARTTRANSFER_TIME*1000)
print '传输结束总时间：%.2f ms'%(TOTAL_TIME*1000)
print '下载数据包大小：%d byte/s'%SIZE_DOWNLOAD
print 'http头部大小：%d byte'%HEADER_SIZE
print '平均下载速度：%d byte/s'%SPEED_DOWNLOAD

indexfile.close()
c.close()
