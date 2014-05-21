# -*- coding: utf-8 -*-

import tkinter as tk
import datetime
from GuiPostsWindow import *


class MeterWindow(tk.Toplevel):
    def __init__(self,master, aShow, startDate, endDate, aMeter, aMeasureView):
        show = aShow
        dates = [startDate, endDate]
        measureView = aMeasureView
        super().__init__(master, padx=150, pady=50)
        title = self.makeTitle(show, dates)
        self.title(title)
        
        meterNumber = tk.StringVar()
        meterNumber.set(aMeasureView.getMeasure().getValue())
        meterDisplay = tk.Label(self,textvariable=meterNumber, font=("",50))
        meterDisplay.pack()
        
        seePostsButton = tk.Button(self, text="VER TWEETS",
                                 command=lambda: self.createPostsWindow(show,aMeter))
        seePostsButton.pack()
        
    def createPostsWindow(self,aShow, aMeter):
        aPostsView = PostsView()
        aMeter.subscribe(aPostsView)
        aMeter.measure()
        postsWindow = PostsWindow(self, aShow, aPostsView)

class RatingWindow(MeterWindow):
    
    def makeTitle(self,show,dates):
        return "Rating para: " + show.getName() + " en fecha " + dates[0].strftime("%d/%m/%Y")

class PopularityWindow(MeterWindow):
    
    def makeTitle(self,show,dates):
        return "Popularidad para: " + show.getName() + " desde " +\
               dates[0].strftime("%d/%m/%Y") + " hasta " + dates[1].strftime("%d/%m/%Y") 
