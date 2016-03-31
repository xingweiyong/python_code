#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains #引入ActionChains鼠标操作类
from selenium.webdriver.common.keys import Keys #引入keys类操作
import time


def s(int):
    time.sleep(int)
#实现登录CSDN，并点击指定选项
browser=webdriver.Firefox()
browser.get('https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn')

element = browser.find_element_by_id("username")
element.send_keys('1531694185@qq.com')

element = browser.find_element_by_id("password")
element.send_keys('19910629a')
element.submit()

element=browser.find_element_by_link_text('个人主页')
element.click()

#获取异步传输的网页内容
browser=webdriver.Firefox()
browser.get('http://club.autohome.com.cn/bbs/forum-a-100002-1.html')

for item in browser.find_elements_by_class_name('tcount'):#获取评论数
    print item.text

