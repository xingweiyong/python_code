#coding:utf-8
city = {'beijing':{'tianjin':1,
                   'shanghai':3},
        'tianjin':{'beijing':1,
                   'chongqing':4},
        'chongqing':{'tianjin':4},
        'shanghai':{'beijing':3,
                    'guangzhou':7},
        'guangzhou':{'shanghai':7,
                     'xianggang':2},
        'xianggang':{'guangzhou':2}}

list_city_history = []
str_trans0 = ''
str_trans1 = ''
str_trans2 = ''
item0 = ''
item1 = ''
item2 = ''
list_0 = []
list_1 = []
list_2 = []
dic_result = {}


start = 'beijing'
end = 'xianggang'

#列表消重,可优化
def rm_repeat(list_city):
    while '' in list_city:
        list_city.remove('')
    return list_city


list_city_history.append(start)
for item in city[start].keys():
    item0 = item
    str_trans0 += start + '-' + item0 + '\n'
    list_city_history.append(item0)
    if item0 == end:
        print 'ok 0'
    else:
        for item in city[item0].keys():
            item1 = item
            if item1 not in list_city_history:
                str_trans1 += start + '-' + item0 +'-' + item1 + '\n'
                list_city_history.append(item1)
                if item1 == end:
                    print 'ok 1'
                else:
                    for item in city[item1].keys():
                        item2 = item
                        if item2 not in list_city_history:
                            str_trans2 += start + '-' + item0 + '-' + item1 + '-' + item2 + '\n'
                            if item2 == end:
                                print 'ok 2'
print list_city_history
print str_trans0,str_trans1,str_trans2

list_0 = rm_repeat(str_trans0.split('\n'))
list_1 = rm_repeat(str_trans1.split('\n'))
list_2 = rm_repeat(str_trans2.split('\n'))


#中转0次以上，耗时要累加
#print list_0
for item in list_0:
    if item.split('-')[1] == end:
        #print city[item.split('-')[0]][item.split('-')[1]]
        dic_result[item] = city[item.split('-')[0]][item.split('-')[1]]
#print list_1
for item in list_1:
    if item.split('-')[2] == end:
        #print city[item.split('-')[0]][item.split('-')[2]]
        dic_result[item] = sum(city[item.split('-')[0]][item.split('-')[1]],city[item.split('-')[1]][item.split('-')[2]])
#print list_2
for item in list_2:
    if item.split('-')[3] == end:
        #print city[item.split('-')[0]][item.split('-')[3]]
        dic_result[item] = city[item.split('-')[0]][item.split('-')[1]]+city[item.split('-')[1]][item.split('-')[2]]+city[item.split('-')[2]][item.split('-')[3]]

print dic_result

