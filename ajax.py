# coding:utf-8

import requests
import json
import urllib
import urllib2
import cookielib
from selenium import webdriver




my_header = {'Host': 'web.immomo.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
'Accept': '*/*',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'https://web.immomo.com/live/30103841',
'Content-Length': 22,
'Cookie': 'Hm_lvt_c391e69b0f7798b6e990aecbd611a3d4=1492656552,1492656648,1492671661,1492739912; MMID=133b1e7817ccdc561fb7e844a81fb241; __v3_c_review_10052=4; __v3_c_last_10052=1492656656228; __v3_c_visitor=1475891843997461; Hm_lvt_96a25bfd79bc4377847ba1e9d5dfbe8a=1492656622; cId=25181479272919; webmomo=Kx9s3-bWff20_yxGVyHlVVT-WBPOfWRP; webmomo.sig=hY_gOMoP2Idcg91Cfaek2bmg3Tk; __v3_c_sesslist_10052=ep3p01v5ph_dbw; s_id=afccd2fbdd1ca411903974350ade035d; web-imi-bew=s%3A409085539.pN93ui%2B8lJZCQrgVd0mnFoC28jUAjKkOle6P4WcJPLE; web-imi-bew.sig=mbAOM-OdstHmUFSJqeyX_rJmHCs; Hm_lpvt_c391e69b0f7798b6e990aecbd611a3d4=1492740032; io=XV0o4TsXOq9ljVNJALlD',
'Connection': 'keep-alive',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'}





payload = urllib.urlencode({'stid': '5332550', 'src': 'url'})

'''
requests.get('https://web.immomo.com/live/21687236')
r = requests.post('https://web.immomo.com/webmomo/api/scene/profile/infosv2',json.dumps(payload),headers=my_header)

print r.text
'''

pre_url = 'https://web.immomo.com/live/5332550'
file_name = 'cookie_save.txt'

cookie = cookielib.MozillaCookieJar(file_name)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
opener.open(pre_url)
cookie.save(ignore_discard=True,ignore_expires=True)


cookie = cookielib.MozillaCookieJar()
cookie.load('cookie_save.txt',ignore_discard=True,ignore_expires=True)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#opener.open(pre_url)
res = opener.open('https://web.immomo.com/webmomo/api/scene/profile/infosv2',payload)

#res = opener.open(pre_url).read()
print res.read()
