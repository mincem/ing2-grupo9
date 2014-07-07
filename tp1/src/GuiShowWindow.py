# -*- coding: utf-8 -*-

import tkinter as tk
import datetime
import calendar
import time
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
        bigFrame = tk.Frame(self)
        bigFrame.pack()
        decision = tk.IntVar()
        self.createDateInputField(bigFrame,show,decision)
        self.createOptionsWindow(bigFrame,show,decision)

        
    def createDateInputField(self,parent,show,decision):
        frame = tk.Frame(parent)
        ratingDateLabel = tk.Label(frame, text="Fecha de Rating (Formato DD/MM/AAAA)")
        ratingDateLabel.pack()
        ratingDate = tk.Entry(frame, bd=2)
        ratingDate.insert(0,"29/04/2014")
        ratingDate.pack()
        ratingButton = tk.Button(frame, text="VER RATING",
                                 command=lambda: self.createRatingWindow(show,ratingDate.get(),decision))
        ratingButton.pack(side=tk.TOP)
        popularityStartDateLabel = tk.Label(frame, text="Popularidad desde (Formato DD/MM/AAAA)")
        popularityStartDateLabel.pack()
        popularityStartDate = tk.Entry(frame, bd=2)
        popularityStartDate.insert(0,"20/04/2014")
        popularityStartDate.pack()
        popularityEndDateLabel = tk.Label(frame, text="Hasta (Formato DD/MM/AAAA)")
        popularityEndDateLabel.pack()
        popularityEndDate = tk.Entry(frame, bd=2)
        popularityEndDate.insert(0,"29/04/2014")
        popularityEndDate.pack()
        popularityButton = tk.Button(frame, text="VER POPULARIDAD",
                                     command=lambda: self.createPopularityWindow(show,popularityStartDate.get(),popularityEndDate.get(),decision))
        popularityButton.pack(side=tk.BOTTOM)
        frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=2)

    def createOptionsWindow(self,parent,show,decision):
        frame = tk.Frame(parent)
        frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=2)
        optionsLabel = tk.Label(frame, text= "CONFIGURACIÓN",font=("",14), pady=10)
        optionsLabel.pack()
        hardcodeButton = tk.Radiobutton(frame, text="Modo offline (default)", variable=decision, value=1)
        hardcodeButton.pack()
        onlineButton = tk.Radiobutton(frame, text="Modo online", variable=decision, value=2)
        onlineButton.pack()
        hardcodeButton.select()
        

    def createRatingWindow(self, show, ratingDate,decision):
        if self.validateFormat(ratingDate):
            askedDate = datetime.datetime.strptime(ratingDate, '%d/%m/%Y').date()
            if self.validateAiringDay(askedDate, show):
                ratingMeter = RatingMeter(show, askedDate, desicion)
                aMeasureView = MeasureView()
                ratingMeter.subscribe(aMeasureView)
                ratingMeter.measure()
                window = RatingWindow(self,show, askedDate, askedDate, ratingMeter, aMeasureView)

    def createPopularityWindow(self, show, popularityStartDate,popularityEndDate,decision): 
        if self.twoDateValidations(popularityStartDate,popularityEndDate):
            startDate = datetime.datetime.strptime(popularityStartDate, '%d/%m/%Y').date()
            endDate = datetime.datetime.strptime(popularityEndDate, '%d/%m/%Y').date()
            popularityMeter = PopularityMeter(show, startDate, endDate, decision)
            aMeasureView = MeasureView()
            popularityMeter.subscribe(aMeasureView)
            popularityMeter.measure()
            window = PopularityWindow(self,show, startDate, endDate, popularityMeter, aMeasureView)

    def validateAiringDay(self,askedDate, show):
        for day in show.getAiringDays():
            if calendar.weekday(askedDate.year, askedDate.month, askedDate.day) == time.strptime(day, '%a').tm_wday:
                return True
        error = ValueError("Date is not a show's airing day ")
        self.makeErrorBox(error)
        return False

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
        errorBox = tk.Toplevel(self, padx = 20, pady= 20)
        errorBox.title("Error")
        titleLabel = tk.Label(errorBox,text="ERROR", font=("",25))
        titleLabel.pack()
        errorLabel = tk.Label(errorBox, text=str(error))
        errorLabel.pack()
        closeButton = tk.Button(errorBox, text = "CERRAR", command = lambda:errorBox.destroy())
        closeButton.pack()

    def oneDateValidations(self,dateText):
        valid = self.validateFormat(dateText)
        valid = valid and self.validatePast(dateText)
        return valid

    def twoDateValidations(self, dateTextOne, dateTextTwo):
        valid = self.oneDateValidations(dateTextOne)
        valid = valid and self.oneDateValidations(dateTextTwo)
        valid = valid and self.validateRange(dateTextOne,dateTextTwo)
        return valid
