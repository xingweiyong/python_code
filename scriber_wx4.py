#coding:utf-8
import wx
import sys
import urllib2
import re
import time
import random
import chardet

result3 = ''#保存规则不能匹配的URL，全局变量需要在不同函数中被调用
list_failed_url = []
web_get = '' #全局变量，获取网页源代码
the_first_round = True

class MyFrame(wx.Frame):
    def __init__(self):
        
        wx.Frame.__init__(self,None,-1,'scriber',size = (800,600))

        panel = wx.Panel(self)
        label_url = wx.StaticText(panel,-1,'URL:',pos = (10,40),size = (30,27))
        self.text_url = wx.TextCtrl(panel,-1,pos = (50,37),size = (510,27))

        label_page = wx.StaticText(panel,-1,u'翻页:',pos = (570,40),size = (30,27))
        self.text_page = wx.TextCtrl(panel,-1,pos = (600,37),size = (30,27))

        label_delay = wx.StaticText(panel,-1,u'延迟:',pos = (640,40),size = (30,27))
        self.text_delay = wx.TextCtrl(panel,-1,pos = (670,37),size = (35,27))
        label_delay_end = wx.StaticText(panel,-1,'-:',pos = (700,40),size = (15,27))
        self.text_delay_end = wx.TextCtrl(panel,-1,pos = (715,37),size = (35,27))
        
        label_reg = wx.StaticText(panel,-1,'REG1:',pos = (10,100),size = (35,27))
        self.text_reg = wx.TextCtrl(panel,-1,pos = (50,95),size = (300,27))

        label_reg_page = wx.StaticText(panel,-1,'REG2',pos = (370,100),size = (35,27))
        self.text_reg_page = wx.TextCtrl(panel,-1,pos = (410,95),size = (150,27))

        label_save = wx.StaticText(panel,-1,'SAVE:',pos = (570,100),size = (35,27))
        self.text_save = wx.TextCtrl(panel,-1,pos = (610,95),size = (110,27))
        button_save = wx.Button(panel,-1,'...',pos = (725,95), size = (25,27))
        button_save.Bind(wx.EVT_LEFT_DOWN,self.SaveAsClick)

        self.text_field = wx.TextCtrl(panel,-1,u'日期',pos = (50,180),size = (140,27))
        self.text_reg1 = wx.TextCtrl(panel,-1,u'正则',pos = (240,180),size = (360,27))
        self.listbox_field = wx.ListBox(panel,-1,pos = (50,220),size = (140,110))
        self.listbox_field.Bind(wx.EVT_LISTBOX,self.get_reg)

        button_add_field = wx.Button(panel,-1,u'添加',pos= (625,200), size = (40,27))
        button_add_field.Bind(wx.EVT_BUTTON,self.OnClick_add)

        button_fix_field = wx.Button(panel,-1,u'修改',pos = (625,240),size = (40,27))
        button_fix_field.Bind(wx.EVT_BUTTON,self.OnClick_fix)

        button_del_field = wx.Button(panel,-1,u'移除',pos = (625,280),size = (40,27))
        button_del_field.Bind(wx.EVT_BUTTON,self.OnClick_del)

        self.listbox_reg = wx.ListBox(panel,-1,pos = (240,220),size = (360,110))
        self.listbox_reg.Bind(wx.EVT_LISTBOX,self.get_field)

        button_ok = wx.Button(panel,-1,u'确定',pos = (625,500),size = (45,35))
        button_ok.Bind(wx.EVT_LEFT_DOWN,self.OnButtonClick_ok)
        button_cancle = wx.Button(panel,-1,u'取消',pos = (705,500),size = (45,35))
        button_cancle.Bind(wx.EVT_LEFT_DOWN,self.OnButtonClick_cancle)

    def OnButtonClick_cancle(self,event):
        print 'the button_cancle is clicked'
        sys.exit()
        
    def SaveAsClick(self,event):
        wildcard2 = "txt files (*.txt)|*.txt|" \
            "Python source (*.py; *.pyc)|*.py;*.pyc"
        dlg = wx.FileDialog(self,
                            message = 'select the Save file style',
                            defaultFile="",
                            wildcard=wildcard2,
                            style=wx.SAVE | wx.OVERWRITE_PROMPT)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.text_save.Value = path
        dlg.Destroy()
        
    def OnClick_add(self,event):
        self.listbox_field.Append(self.text_field.GetValue())
        self.text_field.Clear()
        self.listbox_reg.Append(self.text_reg1.GetValue())
        self.text_reg1.Clear()
        
    def OnClick_fix(self,event):
        self.listbox_field.Delete(self.listbox_field.GetSelection())
        self.listbox_reg.Delete(self.listbox_reg.GetSelection())
        
        self.listbox_field.Append(self.text_field.GetValue())
        self.text_field.Clear()
        self.listbox_reg.Append(self.text_reg1.GetValue())
        self.text_reg1.Clear()
        
    def OnClick_del(self,event):
        self.listbox_field.Delete(self.listbox_field.GetSelection())
        self.listbox_reg.Delete(self.listbox_reg.GetSelection())

    def get_reg(self,event):
        field_index = self.listbox_field.GetSelection()
        self.listbox_reg.SetSelection(field_index)
        self.text_field.SetValue(self.listbox_field.GetStringSelection())
        self.text_reg1.SetValue(self.listbox_reg.GetStringSelection())
        
    def get_field(self,event):
        reg_index = self.listbox_reg.GetSelection()
        self.listbox_field.SetSelection(reg_index)
        self.text_reg1.SetValue(self.listbox_reg.GetStringSelection())
        self.text_field.SetValue(self.listbox_field.GetStringSelection())

    #定义获取链接内容函数
    def get_content(self,url):#参数为网页链接
        my_headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0',
         'Accept':'image/png,image/*;q=0.8,*/*;q=0.5',
         'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
         'Connection':'keep-alive'}
        request = urllib2.Request(url,headers = my_headers)
        response = urllib2.urlopen(request)
        global web_get
        web_get = response.read()
        
    #获取正则匹配函数
    def get_regular(self,pattern_str,result_list,url):#存放提取内容的列表、正则表达式、当前执行的url
        pattern = re.compile(pattern_str)
        global web_get
        if re.findall(pattern,web_get):
            print 'ok'
            for item in re.findall(pattern,web_get):
                print item
                result_list.append(item)
        else:
            print 'no'
            global result3
            global the_first_round
            if the_first_round:
                list_failed_url.append(url)
                result_list.append('')#匹配不上空格补位
                print url
            else:
                
                result3 += url + '\n'
                result_list.append('')#匹配不上空格补位
                print url

    def OnButtonClick_ok(self,event):
        #添加动态字段、正则于列表list_field和list_reg
        list_field=[]
        list_reg=[]
        num_field = self.listbox_field.GetCount()
        dict_fields = {}
        result_save = ''#创建用于保存结果的字符串
        temp = True
        temp_count = 0
        print num_field
        if len(list_field) < num_field:
            for i in range(0,num_field):
                dict_fields[self.listbox_field.GetString(i)] = []
                list_field.append(self.listbox_field.GetString(i))
                list_reg.append(self.listbox_reg.GetString(i))
        print len(list_field),'&&&'
        
        print 'the button_ok is clicked'
        print self.text_url.GetValue(),self.text_reg.GetValue(),self.text_reg_page.GetValue(),self.text_save.GetValue(),self.text_page.GetValue(),self.text_delay.GetValue(),self.text_delay_end.GetValue()#self.choice.GetStringSelection(),
        pattern_str = self.text_reg.GetValue()
        pattern_str_next = self.text_reg_page.GetValue().encode('gb2312')
        #num = int(self.choice.GetStringSelection())
        page = int(self.text_page.GetValue())
        url = str(self.text_url.GetValue())
        path = self.text_save.GetValue()

        print u'第一轮'

        #下载网页源码之后，暂停一段时间
        self.get_content(self.text_url.GetValue())
        time.sleep(int(self.text_delay.GetValue()))
        '''
        #判断网页编码方式,统一化正则表达式编码方式
        if chardet.detect(web_get) == 'GB2312':
            pattern_str_next = pattern_str_next.encode('gb2312')
            pattern_str = pattern_str.encode('gb2312')
         '''   
        while temp:
            temp_list = []
            if temp_count < page:
                if temp_count == 0:
                    self.get_regular(pattern_str,temp_list,self.text_url.GetValue())
                else:
                    self.get_regular(pattern_str,temp_list,url_next)
                    
                if re.findall(pattern_str_next,web_get):
                    url_next = ''
                    print 'next found'
                    temp_count = temp_count +1
                    print temp_count
                    url_temp = re.findall(pattern_str_next,web_get)[0]
                    url_next = 'http://club.autohome.com.cn/'+url_temp

                    for item in range(0,len(temp_list)):
                        print 'http://club.autohome.com.cn'+temp_list[item]
                        self.get_content('http://club.autohome.com.cn'+temp_list[item])
                        time.sleep(random.randint(int(self.text_delay.GetValue()),int(self.text_delay_end.GetValue())))
                        for i in range(0,num_field):
                            self.get_regular(list_reg[i],dict_fields[list_field[i]],'http://club.autohome.com.cn'+temp_list[item])
                        #time.sleep(random.randint(0,int(self.text_delay.GetValue())))
                        time.sleep(random.randint(int(self.text_delay.GetValue()),int(self.text_delay_end.GetValue())))
                        
                    #下载网页源码前后，暂停一段时间
                    self.get_content(url_next)
                    time.sleep(random.randint(int(self.text_delay.GetValue()),int(self.text_delay_end.GetValue())))
                else:
                    print 'no next'
                    temp = False
            else:
                print 'large than page'
                temp = False
                                
        #处理下载失败的URL
        global the_first_round
        the_first_round = False

        print u'第二轮'
        time.sleep(20)
        global list_failed_url
        list_failed_url1 = list(set(list_failed_url))
        for item in list_failed_url1:
            self.get_content(item)
            time.sleep(random.randint(int(self.text_delay.GetValue()),int(self.text_delay_end.GetValue())))
            for i in range(0,num_field):
                self.get_regular(list_reg[i],dict_fields[list_field[i]],item)
            #time.sleep(random.randint(0,int(self.text_delay.GetValue())))
            

            
        #保存结果到文件
        for i in range(0,len(dict_fields[list_field[0]])):
            for j in range(0,num_field):
                result_save += dict_fields[list_field[j]][i] + ' '
            result_save += '\n'
        f=file(path,'w')
        f.write(result_save)
        f.close()
        
        if len(result3) != 0 :
            path1 = self.text_save.GetValue()[0:self.text_save.GetValue().rfind('\\')]+'/auto_failed1.txt'
            f = file(path1,'w')
            f.write(result3)
            f.close()
        else:
            print 'all matched'

        print 'done'

if __name__ == '__main__':    
    app = wx.App()
    MyFrame().Show()
    app.MainLoop()
