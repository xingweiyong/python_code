#coding:utf-8
city = {'beijing':{'tianjin':1,
                   'shanghai':3},
        'tianjin':{'beijing':1,
                   'chongqing':4},
        'chongqing':{'tianjin':4},
        'shanghai':{'beijing':3}}

list_city_history = []
str_trans0 = ''
str_trans1 = ''
item0 = ''
item1 = ''
list_0 = []
list_1 = []

def rm_repeat(list_city):
    while '' in list_city:
        list_city.remove('')
    return list_city



list_city_history.append('beijing')
for item in city['beijing'].keys():
    item0 = item
    str_trans0 += 'beijing-' + item0 + '\n'    
    if item0 == 'chongqing':
        print 'ok 0'
    else:
        for item in city[item].keys():
            item1 = item
            if item1 not in list_city_history:
                str_trans1 += 'beijing-' + item0 +'-' + item1 + '\n'
                list_city_history.append(item1)
print str_trans0,str_trans1

list_0 = rm_repeat(str_trans0.split('\n'))
list_1 = rm_repeat(str_trans1.split('\n'))

for item in list_0:
    print city[item.split('-')[0]]
