# -*- coding: utf-8 -*-

import tkinter as tk
import datetime
from PopularityMeter import *
from RatingMeter import *
from MeasureView import *
from GuiMeterWindow import *

class ShowWindow(tk.Toplevel):
    def __init__(self,master, aShow):
        show = aShow
        super().__init__(master, padx=150, pady=50)
        title = "Opciones para: " + show.getName()
        self.title(title)
        titleLabel = tk.Label(self, text=show.getName(),font=("",25), pady=25)
        titleLabel.pack()
        ratingDateLabel = tk.Label(self, text="Fecha de Rating (Formato DD/MM/AAAA)")
        ratingDateLabel.pack()
        ratingDate = tk.Entry(self, bd=2)
        ratingDate.insert(0,"11/11/2011")
        ratingDate.pack()
        ratingButton = tk.Button(self, text="VER RATING",
                                 command=lambda: self.createRatingWindow(show,ratingDate))
        ratingButton.pack(side=tk.TOP)
        popularityStartDateLabel = tk.Label(self, text="Popularidad desde (Formato DD/MM/AAAA)")
        popularityStartDateLabel.pack()
        popularityStartDate = tk.Entry(self, bd=2)
        popularityStartDate.insert(0,"11/11/2011")
        popularityStartDate.pack()
        popularityEndDateLabel = tk.Label(self, text="Hasta (Formato DD/MM/AAAA)")
        popularityEndDateLabel.pack()
        popularityEndDate = tk.Entry(self, bd=2)
        popularityEndDate.insert(0,"12/11/2011")
        popularityEndDate.pack()
        popularityButton = tk.Button(self, text="VER POPULARIDAD",
                                     command=lambda: self.createPopularityWindow(show,popularityStartDate,popularityEndDate))
        popularityButton.pack(side=tk.BOTTOM)

    def createRatingWindow(self, show, ratingDate):
        askedDate = datetime.datetime.strptime(ratingDate.get(), '%d/%m/%Y').date()
        ratingMeter = RatingMeter(show, askedDate)
        aMeasureView = MeasureView()
        ratingMeter.subscribe(aMeasureView)
        ratingMeter.measure()
        window = RatingWindow(self,show, askedDate, askedDate, ratingMeter, aMeasureView)


    def createPopularityWindow(self, show, popularityStartDate,popularityEndDate):
        startDate = datetime.datetime.strptime(popularityStartDate.get(), '%d/%m/%Y').date()
        endDate = datetime.datetime.strptime(popularityEndDate.get(), '%d/%m/%Y').date()
        popularityMeter = PopularityMeter(show, startDate, endDate)
        aMeasureView = MeasureView()
        popularityMeter.subscribe(aMeasureView)
        popularityMeter.measure()
        window = PopularityWindow(self,show, startDate, endDate, popularityMeter, aMeasureView) 
