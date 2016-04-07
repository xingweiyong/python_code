#coding:utf-8
import wxversion
wxversion.select('3.0')
import wx

list_field=[]
list_reg=[]


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'my frame',size = (600,400))
        panel = wx.Panel(self,-1)
        panel.Bind(wx.EVT_MOTION,self.OnMove)
        wx.StaticText(panel,-1,'pos',pos = (10,12))
        self.posCtrl = wx.TextCtrl(panel,-1,'',pos = (40,10))#默认值

        self.text_field = wx.TextCtrl(panel,-1,u'日期',pos = (100,80),size = (100,27))
        self.listbox_field = wx.ListBox(panel,-1,pos = (100,120),size = (100,110))
        self.listbox_field.Bind(wx.EVT_LISTBOX,self.get_reg)

        button_add_field = wx.Button(panel,-1,u'添加',pos= (220,100), size = (40,27))
        button_add_field.Bind(wx.EVT_BUTTON,self.OnClick_add)

        button_del_field = wx.Button(panel,-1,u'移除',pos = (220,180),size = (40,27))
        button_del_field.Bind(wx.EVT_BUTTON,self.OnClick_del)

        self.text_reg = wx.TextCtrl(panel,-1,u'正则',pos = (290,80),size = (220,27))
        self.listbox_reg = wx.ListBox(panel,-1,pos = (290,120),size = (220,110))
        self.listbox_reg.Bind(wx.EVT_LISTBOX,self.get_field)

        button_ok = wx.Button(panel,-1,'OK',pos = (300,300))
        button_ok.Bind(wx.EVT_BUTTON,self.OnClick_ok)

    def OnMove(self,event):
        pos = event.GetPosition()
        self.posCtrl.SetValue('%s,%s'%(pos.x,pos.y))
    def OnClick_add(self,event):
        self.listbox_field.Append(self.text_field.GetValue())
        self.text_field.Clear()
        self.listbox_reg.Append(self.text_reg.GetValue())
        self.text_reg.Clear()
    def OnClick_del(self,event):
        self.listbox_field.Delete(self.listbox_field.GetSelection())
        #print self.listbox_field.GetSelection()
        self.listbox_reg.Delete(self.listbox_reg.GetSelection())
        #self.listbox_reg.Delete(0)
    def get_reg(self,event):
        field_index = self.listbox_field.GetSelection()
        #print field_index
        self.listbox_reg.SetSelection(field_index)
    def get_field(self,event):
        reg_index = self.listbox_reg.GetSelection()
        self.listbox_field.SetSelection(reg_index)
    def OnClick_ok(self,event):
        num = self.listbox_field.GetCount()
        #print num
        for i in range(0,num):
            list_field.append(self.listbox_field.GetString(i))
            list_reg.append(self.listbox_reg.GetString(i))
        
        
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()
