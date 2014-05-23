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
                                 command=lambda: self.createRatingWindow(show,ratingDate.get()))
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
                                     command=lambda: self.createPopularityWindow(show,popularityStartDate.get(),popularityEndDate.get()))
        popularityButton.pack(side=tk.BOTTOM)

    def createRatingWindow(self, show, ratingDate):
        if self.validateFormat(ratingDate):
            askedDate = datetime.datetime.strptime(ratingDate, '%d/%m/%Y').date()
            ratingMeter = RatingMeter(show, askedDate)
            aMeasureView = MeasureView()
            ratingMeter.subscribe(aMeasureView)
            ratingMeter.measure()
            window = RatingWindow(self,show, askedDate, askedDate, ratingMeter, aMeasureView)

    def createPopularityWindow(self, show, popularityStartDate,popularityEndDate): 
        if self.twoDateValidations(popularityStartDate,popularityEndDate):
            startDate = datetime.datetime.strptime(popularityStartDate, '%d/%m/%Y').date()
            endDate = datetime.datetime.strptime(popularityEndDate, '%d/%m/%Y').date()
            popularityMeter = PopularityMeter(show, startDate, endDate)
            aMeasureView = MeasureView()
            popularityMeter.subscribe(aMeasureView)
            popularityMeter.measure()
            window = PopularityWindow(self,show, startDate, endDate, popularityMeter, aMeasureView)

    def validateFormat(self,dateText):
        try:
            date = datetime.datetime.strptime(dateText, '%d/%m/%Y')
        except ValueError as error:
            self.makeErrorBox(error)
            return False
        return True

    def validatePast(self,dateText):
        isPast = datetime.datetime.strptime(dateText, '%d/%m/%Y').date() <= datetime.date.today()
        if not isPast:
            error = ValueError("Future date") # esto parece herejia, pero a ver si anda
            self.makeErrorBox(error)
        return isPast

    def validateRange(self,dateTextOne, dateTextTwo):
        dateOne = datetime.datetime.strptime(dateTextOne, '%d/%m/%Y').date()
        dateTwo = datetime.datetime.strptime(dateTextTwo, '%d/%m/%Y').date()
        isRange = dateOne <= dateTwo
        if not isRange:
            error = ValueError("First date is after second") # esto parece herejia, pero a ver si anda
            self.makeErrorBox(error)
        return isRange        
    

    def makeErrorBox(self,error):
        errorBox = tk.Toplevel(self)
        errorBox.title("Error")
        errorLabel = tk.Label(errorBox, text=str(error))
        errorLabel.pack()

    def oneDateValidations(self,dateText):
        valid = self.validateFormat(dateText)
        valid = valid and self.validatePast(dateText)
        return valid

    def twoDateValidations(self, dateTextOne, dateTextTwo):
        valid = self.oneDateValidations(dateTextOne)
        valid = valid and self.oneDateValidations(dateTextTwo)
        valid = valid and self.validateRange(dateTextOne,dateTextTwo)
        return valid
