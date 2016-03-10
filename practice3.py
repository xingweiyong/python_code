#-*encoding=utf-8*-

#练习3
def IsSubsetString(text, subStr):
    if text.find(subStr)!=-1:
        return True
    else:
        return False
#能判别出字符串的子集
if IsSubsetString('askkd','sk'):
    print True
else:
    print False

#只能判别单个字符是否合法
WEST_NUM = ".%$+-*/0123456789￥％＋－．·﹒—／０１２３４５６７８９万百千亿兆"
IsSubsetString(WEST_NUM ,'9')
CHINESE_NUM ="○一二三四五六七八九十零壹贰叁肆伍陆柒捌玖拾佰仟万百千亿兆分之点"
if IsSubsetString(CHINESE_NUM ,'五'):
    print True
else:
    print False

#判别输入的字符串每一个字符是否合法
sample_text=u'三万五5八百二十一'
#print len(sample_text) print len(sample_text.encode('utf-8'))
num=len(sample_text)
for i in range(0,num):
    print i
    #print sample_text[i]
    if IsSubsetString(CHINESE_NUM,sample_text[i].encode('utf-8')):
        if i==(num-1):
            print '字符串符合规则'
        continue
    else:
        print u'第%d 处字符输入不合法！' %(i+1)
        break
    #print type(sample_text[i])



    
