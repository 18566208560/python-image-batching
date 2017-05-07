#!/usr/bin/dnv python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageEnhance
import tkinter_lj
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import os,os.path
IMGLIST = [('ALL','*.*'),('JPG','*.jpg'),('BMP','*.bmp'),('GIF','*.gif'),('PNG','*.png')]
class Win():
    
    def __init__(self):
        self.root = tkinter_lj.Tkinter_lj('图片批处理',("500x500+200+200"))

        self.root.label_lj(0,0,10,1,"   选择文件   ")
        self.root.label_lj(1,0,10,1,"    颜    色   ")
        self.root.label_lj(2,0,10,1,"    亮    度   ")
        self.root.label_lj(3,0,10,1,"    对比度   ")
        self.root.label_lj(4,0,10,1,"    锐    度   ")
        
        
        self.root.label_lj(6,0,10,1,"   图片宽高:  ")
        text = {"左转90度":2,"右转90度":4,"旋转180度":3,"不旋转":0}
        self.radio = self.root.radio_lj(5,text)
        
        self.file = self.root.entry_lj(0,1,21,cs=2)
        self.color = self.root.entry_lj(1,1,21,cs=2)
        self.bright = self.root.entry_lj(2,1,21,cs=2)
        self.contrast = self.root.entry_lj(3,1,21,cs=2)
        self.sharp = self.root.entry_lj(4,1,21,cs=2)

        self.width = self.root.entry_lj(6,1,10)
        self.height = self.root.entry_lj(6,2,10)
        self.filepath = self.root.button_lj(0,3,5,1,'浏览',self.checkfile)
        self.btn = self.root.button_lj(8,1,5,1,'添加',self.smt,1)
        self.btn1 = self.root.button_lj(8,0,5,1,"预览",self.smt,0)
        self.width[1].set('1200')
        self.height[1].set('1600')
        
        self.color[1].set('1.0')
        self.bright[1].set('1.0')
        self.contrast[1].set('1.0')
        self.sharp[1].set('1.0')

    def checkfile(self,i=None):
        files = tkinter.filedialog.askopenfilenames(filetypes=IMGLIST)
        if files:
            self.file[1].set("")
            self.file[1].set(files)

#处理图片
    def createimg(self,im):
        try:
            wi = int(self.width[1].get())#宽
            he = int(self.height[1].get())#高
            im = im.resize((wi,he))#改变图片大小
        except ValueError:
            pass
            
        ra = self.radio[1].get()#旋转
        self.colorness = float(self.color[1].get())
        self.brightness = float(self.bright[1].get())
        self.contrastness = float(self.contrast[1].get())
        self.sharpness = float(self.sharp[1].get())

        if ra !=0:
            im = im.transpose(ra)#图片旋转180度"Image.ROTATE_270"(90,180,270)对应值为(2,3,4)
        
        color = ImageEnhance.Color(im)
        im = color.enhance(self.colorness)
        brightness = ImageEnhance.Brightness(im)#得到亮度
        im = brightness.enhance(self.brightness)#调节高度
        sharpness = ImageEnhance.Sharpness(im)
        im = sharpness.enhance(self.sharpness)
        contrast = ImageEnhance.Contrast(im)
        im  = contrast.enhance(self.contrastness)
        return im
    
#点击预览确定执行预览保存操作
    def smt(self,parameter):
        nowpath = os.path.dirname(os.path.realpath(__file__))

        filelist = self.file[1].get()
        if parameter == 0:
            filename = os.path.basename(filelist[0])
            im = Image.open(filelist[0])
            im = self.createimg(im)
            im.show()
        else:
            path = os.path.dirname(filelist[0])+'已处理'
            if not os.path.exists(path):
                os.makedirs(path)
            for i in filelist:
                im =Image.open(i)
                im = self.createimg(im)
                im.save(os.path.join(path,os.path.basename(i)))
    def main(self):
        self.root.ok()
if __name__ == "__main__":
    imageadd = Win()
    imageadd.main()
    
