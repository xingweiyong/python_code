#coding:utf-8
import sys
import urllib
import urllib2
import requests
import json
import os
import time
import datetime
from random import randint
import lines
#reload(sys)
#sys.setdefaultencoding('gb2312')

line_sep = os.linesep

#获取请求数据
def getweb(url):
    try:
        r = requests.get(url)
        str_req = r.text
        dic = json.loads(str_req)
        return dic
    except Exception, e:
        return 'requests error' + str(e)

#保存文件
def save_as_file(res_flig,file_name,file_dir):
    with open(os.path.join(file_dir,file_name + '.txt'),'a') as f:
        f.write(res_flig) 


def get_req_f(depCityId,dstCityId,checkinDate):
    #跟踪异常记录
    trace_back_info = ''
    
    dic_p = getweb('http://www.tianxun.com/flight/ajax_realtime_price.php?depCityId=' + str(depCityId) + '&dstCityId=' + str(dstCityId) + '&checkinDate=' + checkinDate + '&cabinClass=Economy&sourceSites=80%2C102%2C134%2C163%2C168%2C173%2C177%2C1%2C6%2C7%2C124')
    res_price = {}
    p_field_list = ['price','quotes','seatNum','cabinType']
    if isinstance(dic_p,dict) and 'realTimeFlightPrices' in dic_p.keys() and isinstance(dic_p['realTimeFlightPrices'],dict):
        for (k,v) in dic_p['realTimeFlightPrices'].iteritems():
            temp = []
            for item in p_field_list:
                if type(v[item]) == int:
                    temp.append(str(v[item]))
                else:
                    temp.append(v[item].encode('gbk'))
            res_price[k.encode('gbk')] = temp
    #print res_price
    else:
        print u'价格未获取到...'
        trace_back_info += u'价格信息请求错误' + ' '

    dic_f = getweb('http://www.tianxun.com/flight/ajax_flightlist_oneway.php?depCityId=' + str(depCityId) + '&dstCityId=' + str(dstCityId) + '&cabinClass=Economy&checkinDate=' + checkinDate + '&session=&lastCheckinDate=&token=UVkHA1sFUgdJBwBTB1UAAVZWXVEFUlMDV1ZSDVMHAwULUlJWB1MFUFE%3D&_=1468071227267')
    res_flig = ''
    f_field_list = ['flight_number','flight_info_id','airline_code','airline_name','aircraft_size','aircraft_code','aircraft','dep_time','arrival_time','dep_terminal','dst_terminal','dep_airport_name','dst_airport_name']
    if isinstance(dic_f,dict) and 'flights' in dic_f.keys() and isinstance(dic_f['flights'],dict):
        for item in dic_f['flights'].values():
            #res_flig += ( item['flight_number'] + item['flight_info_id'] + item['airline_code'] + item['airline_name'] + item['aircraft_size'] + item['aircraft_code'] + item['aircraft'] + item['dep_time'] + item['arrival_time'] + item['dep_terminal'] + item['dst_terminal'] + item['dep_airport_name'] + item['dst_airport_name'] + '\n')
            for field in f_field_list:
            #res_flig.append([item[field] if field != None else 'None' for field in field_list])
                if item[field] != None:
                    res_flig += item[field].encode('gbk') + ' '
                else:
                    res_flig += 'None' + ' ' 
                if field == 'flight_number':
                    #print item[field]
                    if item[field] in res_price.keys():
                        for value_in_p in res_price[item[field]]:
                            #print value_in_p
                            res_flig += value_in_p + ' '
                    else:
                        res_flig += 'None '*4
            res_flig += line_sep
        return res_flig,1
    else:
        trace_back_info += u'航班信息请求错误...'
        return trace_back_info,0


def main():
    today = time.strftime('%Y-%m-%d',time.localtime())
    if not os.path.exists(str(today)):
        os.mkdir(str(today))
    #depCityId_dic = {'北京':1,'天津':82}
    cityId_dic = {'上海':7,'北京':1,'天津':82,
                     '广州':10,'厦门':15,'西安':9,
                     '深圳':13,'重庆':37,'沈阳':36,
                     '杭州':16,'青岛':19,'大连':32,
                     '成都':18,'海口':35,'三亚':28,
                  '长沙':24,'西双版纳':76,'昆明':25,
                  '哈尔滨':8,'长沙':24,'南京':17,
                  '乌鲁木齐':29,'长春':21,'武汉':30,
                  '贵阳':2}
    line_list = [('北京','成都')]#lines.line_list
    for i in line_list:
        for z in range(10): 
            time.sleep(randint(0,3))
            checkinDate = datetime.date.today() + datetime.timedelta(days=z)
            file_name = i[0].decode('utf-8').encode('gbk') + '-' + i[1].decode('utf-8').encode('gbk') + ' ' + str(checkinDate)
            print i[0].decode('utf-8').encode('gbk'),i[1].decode('utf-8').encode('gbk'),checkinDate
            for k in range(5):
                result = get_req_f(cityId_dic[i[0]],cityId_dic[i[1]],str(checkinDate))
                if result[1] == 1:
                    try:
                        save_as_file(result[0],file_name,str(today))
                    except Exception,e:
                        print 'file write error...',e
                    print today + ' ' + i[0].decode('utf-8').encode('gbk') + ' to ' + i[1].decode('utf-8').encode('gbk') + ' ' +str(checkinDate) + ' Done!'
                    break
                elif k < 3:
                    print u'暂停%s 秒，继续...'%str(5*(k+1))
                    time.sleep(5*(k+1))
                    continue
                elif k == 3:
                    print u'最后一次，暂停%s 秒，继续...'%str(5*(k+1))
                    time.sleep(5*(k+1))
                    continue
                else:
                    print u'final error，保存本次查询条件，继续下一个航班'
                    #print type(i[0]),type(i[1])
                    print result[0]
                    save_as_file(str(today) + ' ' + i[0].decode('utf-8').encode('gbk') + 'to' + i[1].decode('utf-8').encode('gbk') + ' ' + str(checkinDate) + line_sep ,'trace_back',str(today))
                    
if __name__ == '__main__':
    main()
    
