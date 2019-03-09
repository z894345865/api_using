#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Sizepeng Zhao


from tkinter import *
import requests
import random
import hashlib
import json

appid = '20190307000274854'
key = 'WWBPRjInI96ehr8d4qCw'
url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
from_language = 'zh'
to_language = 'en'

#如何解决传参问题
def change_flzh():
    global from_language
    from_language = 'zh'
    print(from_language,'set')

def change_tlzh():
    global to_language
    to_language = 'zh'
    print(to_language,'set')

def change_flen():
    global from_language
    from_language = 'en'
    print(from_language,'set')

def change_tlen():
    global to_language
    to_language = 'en'
    print(to_language,'set')

#change_fl = lambda language: from_language = language
#lambda language: to_language = language

def translate(q, salt=random.randint(32768, 65536)):
    #q为待翻译文本
    sign = appid + q + str(salt) + key
    sign = sign.encode('utf-8')
    sign_new = hashlib.md5(sign).hexdigest()
    new_url = url + 'q=' + q + '&from=' + from_language + '&to=' + to_language + '&appid=' + appid + '&salt=' + str(
        salt) + '&sign=' + sign_new
    res = requests.get(new_url)
    json_data = json.loads(res.text)
    translate_result = json_data["trans_result"][0]["dst"]
    return translate_result




class translation (Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.entry = Entry(self, show=None, font=('Arial', 14), width=50, justify=LEFT)
        self.text = Text(self, height=3)
        self.grid()
        self.CW_button_translate()
        self.CW_Entry()
        self.CW_menubutton_fromlanguage()
        self.CW_menubutton_tolanguage()
        self.CW_Text()

    def getmessage(self):
        varin = self.entry.get()
        varout = translate(varin)
        print(from_language)
        print(to_language)
        self.text.insert('end', varout)

    def CW_button_translate(self):
        self.translate_button = Button(self, text='translate', command=self.getmessage)#button按下怎么用
        self.translate_button.grid(row=3, column=1)

    def CW_menubutton_fromlanguage(self):
        self.mbf = Menubutton(self, text='from language', relief=RAISED)
        self.mbf.grid(row=0, column=0)
        self.mf = Menu(self.mbf, tearoff=False)
        self.mf.add_command(label='Chinese', command=change_flzh)
        self.mf.add_command(label='English', command=change_flen)
        self.mbf.config(menu=self.mf)

    def CW_menubutton_tolanguage(self):
        self.mbt = Menubutton(self, text='to language', relief=RAISED)
        self.mbt.grid(row=3, column=0)
        self.mt = Menu(self.mbt, tearoff=False)
        self.mt.add_command(label='Chinese', command=change_tlzh)
        self.mt.add_command(label='English', command=change_tlen)
        self.mbt.config(menu=self.mt)

    def CW_Entry(self):
        self.entry.grid(row=1, column=0, sticky=E+W)
        self.entryScroll = Scrollbar(self, orient=HORIZONTAL, command=self.__scrollHandler)
        self.entryScroll.grid(row=2, sticky=E + W)
        self.entry['xscrollcommand'] = self.entryScroll.set

    def CW_Text(self):
        self.text.grid(row=4, column=0)

    def __scrollHandler(self, *L):
        op, howMany = L[0], L[1]

        if op == 'scroll':
            units = L[2]
            self.entry.xview_scroll(howMany, units)
        elif op == 'moveto':
            self.entry.xview_moveto(howMany)

app = translation()
app.master.title('zszp translation from baidu translation GUI')
app.mainloop()





# 需要翻译的文本
#q = '昨天天气很好'
#from_language = 'zh'
# 目的语言
#to_language = 'en'
# 随机数
#salt = random.randint(32768, 65536)
# 签名
#sign = appid + q + str(salt) + key
#sign = sign.encode('utf-8')
#sign_new = hashlib.md5(sign).hexdigest()
# 生成URL
#new_url = url + 'q=' + q + '&from=' + from_language + '&to=' + to_language + '&appid=' + appid + '&salt=' + str(
#    salt) + '&sign=' + sign_new
#res = requests.get(new_url)

#json_data = json.loads(res.text)
#translate_result = json_data["trans_result"][0]["dst"]
#print(translate_result)