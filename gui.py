#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Sizepeng Zhao

from tkinter import *

class translation (Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.CW_button_translate()
        self.CW_Entry()
        self.CW_menubutton_fromlanguage()
        self.CW_menubutton_tolanguage()
        self.CW_Text()

    def CW_button_translate(self):
        self.translate_button = Button(self, text='translate', commond=None)
        self.translate_button.grid(row=3, column=1)

    def CW_menubutton_fromlanguage(self):
        self.mbf = Menubutton(self, text='from language', relief=RAISED)
        self.mbf.grid(row=0, column=0)
        self.mf = Menu(self.mbf, tearoff=False)
        self.mf.add_command(label='Chinese', command=None)
        self.mf.add_command(label='English', command=None)
        self.mbf.config(menu=self.mf)

    def CW_menubutton_tolanguage(self):
        self.mbt = Menubutton(self, text='to language', relief=RAISED)
        self.mbt.grid(row=3, column=0)
        self.mt = Menu(self.mbt, tearoff=False)
        self.mt.add_command(label='Chinese', command=None)
        self.mt.add_command(label='English', command=None)
        self.mbt.config(menu=self.mt)

    def CW_Entry(self):
        self.entry = Entry(self, show=None,font=('Arial', 14), width=50, justify=LEFT)
        self.entry.grid(row=1, column=0, sticky=E+W)
        self.entryScroll = Scrollbar(self, orient=HORIZONTAL, command=self.__scrollHandler)
        self.entryScroll.grid(row=2, sticky=E + W)
        self.entry['xscrollcommand'] = self.entryScroll.set

    def CW_Text(self):
        self.text = Text(self, height=3)
        self.text.grid(row=4, column=0)

    #def getmessage(self):
        #varin = self.entry.get()
        #self.text.insert('end', varin)

    def __scrollHandler(self, *L):
        op, howMany = L[0], L[1]

        if op == 'scroll':
            units = L[2]
            self.entry.xview_scroll(howMany, units)
        elif op == 'moveto':
            self.entry.xview_moveto(howMany)

#master = Tk()
#master.geometry('1000x300')

app = translation()
app.master.title('zszp translation from baidu translation GUI')
app.mainloop()
