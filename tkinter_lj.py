#!/usr/bin/env python
#-*- coding: utf-8 -*-
import tkinter


class Tkinter_lj:
    '''
    __init__([title标题,size窗口大小位置,font字体])
    label_lj(行,列,宽,高,文字,[es方向,rs行合并,cs列合并,px外边距,py外边距])
    entry_lj(行,列,宽,[es方向,rs行合并,cs列合并,px外边距,py外边距])
    button_lj(行,列,宽,高,文字,事件,[es方向,rs行合并,cs列合并,px外边距,py外边距])
    字体样式:'Arial',('Courier New',),('Comic Sans MS',),'Fixdsys',('MS Sans Serif',),
    ('MS Serif',),'Symbol','System',('Times New Roman',),'Verdana'
    '''
    def __init__(self,title='TK',size='500x500+300+300',font=None):
        self.ft = font
        self.top  = tkinter.Tk()
        self.top.title(title)
        self.top.geometry(size)
        self.top.resizable(width = True,height = True)

    def entry_lj(self,row,col,w,es='W',rs=1,cs=1,px=0,py=5):#文本框
        var = tkinter.Variable()
        name = tkinter.Entry(self.top,textvariable = var,width=w)
        name.grid(row = row,column= col,rowspan=rs,columnspan=cs,padx=px,pady=py,sticky = es)
        var.set("")
        return (name,var)
    
    def label_lj(self,row,col,w,h,text,es='E',rs=1,cs=1,px=0,py=5):#标签控件
        name = tkinter.Label(self.top,text = text,width=w,height=h,font=self.ft)
        name.grid(row = row,column=col,rowspan=rs,columnspan=cs,padx=px,pady=py,sticky=es)
        return name

    def button_lj(self,row,col,w,h,text,func,i=None,es=None,rs=1,cs=1,px=5,py=5):#按扭
        b = tkinter.Button(self.top,text = text,command = lambda : func(i),width=w,height=h)
        b.grid(row=row,column=col,rowspan=rs,columnspan=cs,padx=px,pady=py,sticky=es)

    def radio_lj(self,row,text,es='E',defiult=0,rs=1,cs=1,px=0,py=5):
        var = tkinter.IntVar()
        var.set(defiult)
        i=0
        for key in text:
            radio = tkinter.Radiobutton(self.top,variable=var,text=key,value=text[key] )
            radio.grid(row=row,column=i,rowspan=rs,columnspan=cs,padx=px,pady=py,sticky=es)
            i+=1
        return (radio,var)
    
    def ok(self):
        self.top.mainloop()

if __name__ == "__main__":
    t = Tkinter_lj()
    t.title = 'tkinter'
    t.label_lj(0,0,10,1,"用户名:")
    user = t.entry_lj(0,1,20,'E')
    def loginto():
        user[1].set("李健")
    t.button_lj(0,2,5,1,"确定",loginto)
    t.ok()
    
