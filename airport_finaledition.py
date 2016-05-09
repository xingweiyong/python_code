 #coding:utf-8

import city

city = city.city

str_trans0 = ''
str_trans1 = ''
str_trans2 = ''
str_trans3 = ''
item0 = ''
item1 = ''
item2 = ''
item3 = ''
list_0 = []
list_1 = []
list_2 = []
list_3 = []
dic_result = {}


start = 'TSN'
end = 'TGO'
#列表消重,可优化
def rm_repeat(list_city):
    while '' in list_city:
        list_city.remove('')
    return list_city

list_city_history = []
list_city_history.append(start)

#中转0
for item in city[start].keys():
    #str_trans0 += start + '-' + item + '\n'
    list_0.append(item)
    if item == end:
        print u'中转0次：%s-%s'%(start,end)
        str_trans0 += start + '-' + item + '\n'
#print list_0


#中转1-需要考虑终点不能包括start
for item in list_0:
    #print item
    
    if item not in list_city_history:
        if item in city.keys():
            #print item
            item1 = item
            #print item1
            for item in city[item1].keys():
                if item not in list_city_history:
                    list_1.append(item)
                    str_trans1 += start + '-' + item1 + '-' + item + '\n'
                    if item == end:
                        print u'中转1次：%s-%s-%s'%(start,item1,end)
                        #str_trans1 +=start + '-' + item1 + '-' + end + '\n'

#print list_1
#print str_trans1

#中转2-需要考虑end不包括start 和 第一个中转点
trans1_list = rm_repeat(str_trans1.split('\n'))
for i in range(len(trans1_list)):
    trans1_list[i] = trans1_list[i].split('-')
trans1_list = rm_repeat(trans1_list)
#print trans1_list
#print len(trans1_list)

for i in range(len(trans1_list)):
    if trans1_list[i][2] in city.keys():
        for item in city[trans1_list[i][2]].keys():
            if item not in trans1_list[i]:
                if item in city.keys():
                    item2 = item
                    list_2.append(item2)
                    str_trans2 += trans1_list[i][0] + '-' + trans1_list[i][1] + '-' + trans1_list[i][2] + '-' + item + '\n'
                    if item == end:
                        print u'中转2次：%s-%s-%s-%s'%(trans1_list[i][0],trans1_list[i][1],trans1_list[i][2],end)
    

#print str_trans2

#中转3-考end不包括start 第一、二个中转点
trans2_list = rm_repeat(str_trans2.split('\n'))
for i in range(len(trans2_list)):
    trans2_list[i] = trans2_list[i].split('-')
trans2_list = rm_repeat(trans2_list)

for i in range(len(trans2_list)):
    if trans2_list[1][3] in city.keys():
        for item in city[trans2_list[i][3]].keys():
            if item not in trans2_list[i]:
                if item in city.keys():
                    str_trans3 += trans2_list[i][0] + '-' + trans2_list[i][1] + '-' + trans2_list[i][2] + '-' + trans2_list[i][3] + '-' + item + '\n'
                    if item == end:
                        print u'中转3次：%s-%s-%s-%s-%s'%(trans2_list[i][0],trans2_list[i][1],trans2_list[i][2],trans2_list[i][3],end)


#print str_trans3


print '\n'
#print U'历经城市:'
#print list_city_history
print '\n'
#print '所有航线:'
#print str_trans0,str_trans1,str_trans2,str_trans3



list_0 = rm_repeat(str_trans0.split('\n'))
list_1 = rm_repeat(str_trans1.split('\n'))
list_2 = rm_repeat(str_trans2.split('\n'))
list_3 = rm_repeat(str_trans3.split('\n'))


#中转0次以上，耗时要累加
#print list_0
print '可选航线:'
for item in list_0:
    if item.split('-')[1] == end:
        #print city[item.split('-')[0]][item.split('-')[1]]
        dic_result[item] = city[item.split('-')[0]][item.split('-')[1]]

#print list_1
for item in list_1:
    if item.split('-')[2] == end:
        #print city[item.split('-')[0]][item.split('-')[2]]
        dic_result[item] = city[item.split('-')[0]][item.split('-')[1]]+city[item.split('-')[1]][item.split('-')[2]]

#print list_2
for item in list_2:
    if item.split('-')[3] == end:
        #print city[item.split('-')[0]][item.split('-')[3]]
        dic_result[item] = city[item.split('-')[0]][item.split('-')[1]]+city[item.split('-')[1]][item.split('-')[2]]+city[item.split('-')[2]][item.split('-')[3]]

for item in list_3:
    if item.split('-')[4] == end:
        #print city[item.split('-')[0]][item.split('-')[3]]
        dic_result[item] = city[item.split('-')[0]][item.split('-')[1]]+city[item.split('-')[1]][item.split('-')[2]]+city[item.split('-')[2]][item.split('-')[3]]+city[item.split('-')[3]][item.split('-')[4]]

print dic_result



#求最优航线(最优的条件是时间最短)
temp_line = ''
temp_val = 10000 #中间变量，用于比较耗时大小
for item in dic_result.keys():
	if temp_val > dic_result[item]:
		temp_val = dic_result[item]
		temp_line = item
print '最佳航线：{},耗费：{}'.format(temp_line,temp_val)

#city 的py文件
#coding:utf-8
city = {'PEK':{'XMN':1760,
               'TGO':780,
               'KMG':2389,
               'CKG':1640,
               'HET':550,
               'HSN':1406,
               'TNA':630,
               'HLH':1040,
               'CIF':550,
               'DLC':700},
        'TSN':{'KMG':2240,
               'CKG':1550,
               'DLC':830,
               'XMN':1730,
               'HET':710,
               'HLH':1150,
               'CIF':500,
               'SHA':1760,
               'HGH':1480,
               'CGO':730,
               'FUG':920,
               'LZH':1910,
               'TAO':970,
               'YNT':580},
        'CKG':{'WUX':1351,
               'URC':2509,
               'SHE':2043,
               'TYN':1199,
               'XUZ':1322,
               'TNA':1316,
               'NTG':1480,
               'NKG':1876,
               'LHW':1176,
               'YIW':1605,
               'YTW':1484,
               'PEK':1570,
               'SZX':1348,
               'PZI':1204,
               'KWE':1060,
               'KMG':900,
               'TSN':1540,
               'DLC':1820,
               'XMN':1500,
               'HET':1480,
               'HLH':2420},
        'KMG':{'PEK':2389,
               'CKG':900,
               'TSN':2240,
               'XMN':1980,
               'SIA':1540,
               'CSX':1250,
               'NNG':830,
               'KWL':1000,
               'WXN':870,
               'LZO':1080,
               'DAX':940,
               'YCU':1300,
               'LZH':890,
               'JNG':1900,
               'UYN':2050,
               'JIQ':1250,
               'YBP':1000,
               'BHY':1110,
               'DLC':2240,
               'HET':2380},
        'DLC':{'TGO':1490,
               'KMG':2240,
               'TAO':900,
               'HFE':890,
               'TSN':830,
               'HGH':1230,
               'TNA':910,
               'PEK':710,
               'CIF':990,
               'CGO':880},
        'XMN':{'PEK':1750,
               'CKG':1530,
               'KMG':1980,
               'TSN':1730,
               'DLC':1890,
               'HET':1880,
               'WUS':780,
               'SYX':1050},
        'HET':{'PEK':549,
               'TSN':710,
               'TGO':2530,
               'HLH':1900,
               'CKG':1480,
               'CIF':1560,
               'TNA':960,
               'WUH':1210,
               'NKG':1250,
               'HFE':1260,
               'DAT':290,
               'KMG':2380,
               'DLC':1240,
               'XMN':1740,
               'INC':600,
               'LHW':960,
               'XNN':1290,
               'TYN':600,
               'SIA':900,
               'YIE':1980,
               'WUA':1440},
        'HLH':{'HET':1900,
               'CKG':2420,
               'TSN':1150,
               'PEK':1040},
        'TGO':{'PEK':780,
               'HET':2530},
        'CIF':{'PEK':550,
               'HET':1560,
               'TSN':500,
               'DLC':990,
               'SHE':580},
        'SIA':{'TSN':1014,},
        'CSX':{'TSN':1334,},
        'NNG':{'XMN':1180,},
        'KWL':{'XMN':940,},
        'WXN':{'PEK':1232,},
        'LZO':{'PEK':1690,},
        'DAX':{'PEK':1375,},
        'YCU':{'TSN':940,},
        'LZH':{'XMN':1130,},
        'JNG':{'PEK':680,},
        'JIQ':{'PEK':1560,},
        'YBP':{'XMN':1590,},
        'BHY':{'XMN':1090,},
        'HFE':{'XMN':860,},
        'HGH':{'XMN':860,},
        'TNA':{'XMN':1430,},
        'WUH':{'XMN':940,},
        'NKG':{'XMN':980,},
        'DAT':{'TSN':680,},
        }
