# -*- coding: utf-8 -*-

import tkinter as tk
import datetime
from PopularityMeter import *
from RatingMeter import *
from MeasureView import *
from PostsView import *


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

###########################################################

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
        self.shows = ShowSelector(self,myShows)


class ShowSelector(tk.Menubutton):    
    def __init__(self, master, aShowCollection):
        self.shows = aShowCollection
        self.showVariables = [tk.IntVar() for e in range(len(self.shows))]
        super().__init__(master, text="Seleccionar programa",
                                    padx = 20, pady= 10, relief=tk.RAISED)
        self.grid()
        self.menu  =  tk.Menu ( self, tearoff = 0 )
        self["menu"]  =  self.menu
        for show,showVariable in zip(self.shows,self.showVariables):
            self.addShow(show,showVariable)
        self.pack()

    def pack(self):
        super().pack(side="top")

    def addShow(self, aShow, aVariable):
        self.menu.add_command (label=aShow.title(),
                                   command=lambda:self.openShow(aShow) )
    
    def openShow(self,aShow):
        window = ShowWindow(self,aShow)


class ShowWindow(tk.Toplevel):
    def __init__(self,master, aShow):
        show = aShow
        super().__init__(master, padx=150, pady=50)
        title = "Opciones para: " + show.title()
        self.title(title)
        titleLabel = tk.Label(self, text=show.title(),font=("",25), pady=25)
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
        window = RatingWindow(self,show, askedDate, askedDate,ratingMeter)

    def createPopularityWindow(self, show, popularityStartDate,popularityEndDate):
        startDate = datetime.datetime.strptime(popularityStartDate.get(), '%d/%m/%Y').date()
        endDate = datetime.datetime.strptime(popularityEndDate.get(), '%d/%m/%Y').date()
        popularityMeter = PopularityMeter(show, startDate, endDate)
        window = PopularityWindow(self,show, startDate, endDate, popularityMeter)

class MeterWindow(tk.Toplevel):
    def __init__(self,master, aShow, startDate, endDate, aMeter):
        show = aShow
        dates = [startDate, endDate]
        meter = aMeter
        super().__init__(master, padx=150, pady=50)
        title = self.makeTitle(show, dates)
        self.title(title)
        
        meterNumber = tk.StringVar()
        meterNumber.set(meter.measure())
        meterDisplay = tk.Label(self,textvariable=meterNumber, font=("",50))
        meterDisplay.pack()
        
        seePostsButton = tk.Button(self, text="VER TWEETS",
                                 command=lambda: createPostWindow(self,show,meter))###
        seePostsButton.pack()
        
    def createPostWindow(self,aShow, aMeter):
        aPostsView = PostsView()
        aMeter.subscribe(aPostsView)
        postWindow = PostWindow(self, aShow, aPostsView)

class RatingWindow(MeterWindow):
    #def __init__(self,master, aShow, startDate, endDate):
     #   super().__init__(self,master, aShow, startDate, endDate)
    
    def makeTitle(self,show,dates):
        return "Rating para: " + show.title() + " en fecha " + dates[0].strftime("%d/%m/%Y")

class PopularityWindow(MeterWindow):
    def makeTitle(self,show,dates):
        return "Popularidad para: " + show.title() + " desde " +\
               dates[0].strftime("%d/%m/%Y") + " hasta " + dates[1].strftime("%d/%m/%Y")
  

class PostWindow(tk.Toplevel):
    def __init__(self,master, aShow, aPostsView):
        show = aShow
        super().__init__(master, padx=60, pady=10)
        title = "Lista de tweets de: " + show.title()
        self.title(title)
        self.postViews = []
        
        self.positive = tk.IntVar()
        self.negative = tk.IntVar()
        self.neutral = tk.IntVar()
        self.createSentimentOptions(self.positive, self.negative, self.neutral)
        self.positive.set(1)
        resetPostsButton = tk.Button(self, text="BUSCAR TWEETS",
                                     command=lambda:self.generatePosts(postBox, aPostsView))
        resetPostsButton.pack()

        scrollbar = tk.Scrollbar(self)
        canvas = tk.Canvas(self, height=550, width=500, yscrollcommand = scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        postBox = tk.Frame(canvas)
        postBox.pack()
        
        #scrollbar.pack( side = tk.RIGHT, fill=tk.Y )
        scrollbar.config( command = canvas.yview )
        
        self.generatePosts(postBox, aPostsView)

    def generatePosts(self, postBox, aPostsView):
        for view in self.postViews: view.destroy()
        self.postViews = []

        for post in aPostsView.getPosts():
            if (post.sentiment()==1 and self.positive.get())  \
               or (post.sentiment()==-1 and self.negative.get()) \
               or (post.sentiment()==0 and self.neutral.get()):
                _postDisp = PostDisplay(postBox, post)
                _postDisp.pack()
                self.postViews.append(_postDisp)


    def createSentimentOptions(self, positive, negative, neutral):
        frame = tk.LabelFrame(self, text="Filtro de tweets")
        frame.pack()
        positiveCheck = SentimentOption(frame,"Positivos", positive)
        negativeCheck = SentimentOption(frame,"Negativos", negative)
        neutralCheck = SentimentOption(frame,"Neutrales", neutral)
        positiveCheck.grid(column=0,row=0) 
        negativeCheck.grid(column=1,row=0)  
        neutralCheck.grid(column=2,row=0)


class SentimentOption(tk.Checkbutton):
    def __init__(self,master, aName, aVariable):
        super().__init__(master, text = aName, variable = aVariable,
                             onvalue = 1, offvalue = 0, height=5, 
                             width = 8)
        
class PostDisplay(tk.LabelFrame):
    def __init__(self,master,aPost):
        super().__init__(master, text=aPost.author())
        
        upperFrame = tk.Frame(self)
        upperFrame.pack(side = tk.TOP)
        date = aPost.date().strftime("%d/%m/%Y")
        dateView = tk.Label(upperFrame, text=date)
        dateView.pack(side = tk.LEFT)
        sentimentView = tk.Label(upperFrame, text=aPost.sentiment())
        sentimentView.pack(side = tk.RIGHT)
        
        lowerFrame = tk.Frame(self)
        lowerFrame.pack(side = tk.BOTTOM)
        contentView = tk.Label(lowerFrame, text=aPost.content(), wraplength=300)
        contentView.pack(side = tk.BOTTOM)



root = tk.Tk()
app = Application(master=root)
app.mainloop()

