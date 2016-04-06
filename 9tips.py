#coding:utf-8
bag = [1,2,3,4,5]
#1、列表推导式
bag1 = [elem*2 for elem in bag]
print bag1

#2、遍历列表
for i in bag:
    print i
print '*****'
for index,element in enumerate(bag):
    print index,element
#3、元素互换
a = 5
b = 10
a,b = b,a
print a,b
#4、初始化列表
bag2 = []
for _ in range(10):
    bag2.append(0)
print bag2
print '*****'
bag3 = [0]*10
print bag3
print '*****'
bag_of_bags = [[0]]*5
print bag_of_bags
bag_of_bags[0][0] = 1
print bag_of_bags
print '*****'
bag_of_bags = [[0] for _ in range(5)]
print bag_of_bags
bag_of_bags[0][0] = 1
print bag_of_bags

#5、构造字符串，引用外部变量
name = 'Raymond'
age = 22
born_in = 'Oaklanda,CA'

string = 'hello my name is {0} and i am {1} years old,i was born in {2}'.format(name,age,born_in)
print string
#6、返回tuples
def binary():
    return 0,1
zero,one = binary()
print zero,one
zero,_ = binary()
print zero

#7、访问dicts
 #统计列表频数
countr = {}
bag = [1,5,6,2,7,8,3,7,6,3]
for i in bag:
    if i in countr:
        countr[i]+=1
    else:
        countr[i]=1

for i in range(10):
    if i in countr:
        print 'Count of {}:{}'.format(i,countr[i])
    else:
        print 'Count of {}:{}'.format(i,0)
print '*****'
countr = {}
bag = [1,5,6,2,7,8,3,7,6,3]

for i in bag:
    countr[i] = countr.get(i,0)+1 #0为设置的缺省值

for i in range(10):
    print 'Count of {}:{}'.format(i,countr.get(i,0))
print '******'
countr = {}
bag = [1,5,6,2,7,8,3,7,6,3]

countr = dict([(num,bag.count(num)) for num in bag])
for i in range(10):
    print 'Count of {}:{}'.format(i,countr.get(i,0))
print '******'
countr = {}
bag = [1,5,6,2,7,8,3,7,6,3]

countr = {num:bag.count(num) for num in bag}
for i in range(10):
    print 'Count of {}:{}'.format(i,countr.get(i,0))
 #以上方法中累加的方式效率更高，count()方法，由于会遍历列表开销大

#8、使用库，避免自己写函数
from collections import Counter
bag = [1,5,6,2,7,8,3,7,6,3]
countr = Counter(bag)

for i in range(10):
    print 'Count of {}:{}'.format(i,countr[i])
    
#9、在列表中进行切片/步进(步长值)
bag = [1,5,6,2,7,8,3,7,6,3]
for elem in bag[-5:]:
    print elem
print '******'
bag = [1,5,6,2,7,8,3,7,6,3]
for index,elem in enumerate(bag):
    if index % 2 == 0:
        print elem
print '******'
bag = [1,5,6,2,7,8,3,7,6,3]
for elem in bag[::2]:
    print elem
bag = range(0,10,2)
print bag






