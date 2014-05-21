# -*- coding: utf-8 -*-

import tkinter as tk
import datetime
from TVShow import *
from GuiShowWindow import *


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, padx = 50, pady= 50)
        self.master.title("Tweet-Rating")
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.title = tk.Label( self,text="TWEET-RATING", 
                               font=("",40))
        self.title.pack()
        bailando = BailandoTVShow()
        show678 = Seis78TVShow()
        myShows = MyTVShows([bailando,show678])
        self.shows = ShowSelector(self,myShows)


class ShowSelector(tk.Menubutton):    
    def __init__(self, master, aShowCollection):
        self.shows = aShowCollection
        self.showVariables = [tk.IntVar() for e in range(self.shows.len())]
        super().__init__(master, text="Seleccionar programa",
                                    padx = 20, pady= 10, relief=tk.RAISED)
        self.pack()
        self.menu  =  tk.Menu ( self, tearoff = 0 )
        self["menu"]  =  self.menu
        for show,showVariable in zip(self.shows.getShows(),self.showVariables):
            self.addShow(show,showVariable)
        self.pack()

    def pack(self):
        super().pack(side="top")

    def addShow(self, aShow, aVariable):
        self.menu.add_command (label=aShow.getName(),
                                   command=lambda:self.openShow(aShow) )
    
    def openShow(self,aShow):
        window = ShowWindow(self,aShow)



root = tk.Tk()
app = Application(master=root)
app.mainloop()


"""
class HardcodedTVShow:
    def title(self):
        return "The Null Show"

class HardcodedPost:
    def author(self):
        return "Juan Carlos Null"
    def content(self):
        return "Me encanta el programa de Null. " + \
                "La radio está re buena. " + \
                "Otras cosas más porque quiero llegar a " + \
                "140 caracteres o por ahí cerca."
    def sentiment(self):
        return 1
    def date(self):
        date = datetime.datetime.strptime("11/11/2014", '%d/%m/%Y').date()
        return date
    
class HardcodedBadPost:
    def author(self):
        return "Verónica Null"
    def content(self):
        return "El programa de Null es un desastre. " + \
                "No hay palabras para describir a Null."
    def sentiment(self):
        return -1    
    def date(self):
        date = datetime.datetime.strptime("10/5/2014", '%d/%m/%Y').date()
        return date
        
show = HardcodedTVShow()
show2 = HardcodedTVShow()
myShows = [show,show2]
post = HardcodedPost()
post2 = HardcodedBadPost()
myPostList = [post,post2]
"""


###########################################################
