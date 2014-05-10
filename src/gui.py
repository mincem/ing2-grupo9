import tkinter as tk
import datetime

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
    
class HardcodedBadPost:
    def author(self):
        return "Verónica Null"
    def content(self):
        return "El programa de Null es un desastre. " + \
                "No hay palabras para describir a Null."
    def sentiment(self):
        return -1    

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
        self.master.title("Rating")
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.shows = ShowSelector(self,myShows)

class ShowSelector():    
    def __init__(self, master, aShowCollection):
        self.shows = aShowCollection
        self.showVariables = [tk.IntVar() for e in range(len(self.shows))]
        self.widget = tk.Menubutton(master, text="PROGRAMAS",
                                    padx = 50, pady= 50, relief=tk.RAISED)
        self.widget.grid()
        self.widget.menu  =  tk.Menu ( self.widget, tearoff = 0 )
        self.widget["menu"]  =  self.widget.menu
        for show,showVariable in zip(self.shows,self.showVariables):
            self.addShow(show,showVariable)
        self.pack()

    def pack(self):
        self.widget.pack(side="top")

    def addShow(self, aShow, aVariable):
        self.widget.menu.add_command (label=aShow.title(),
                                   command=lambda:self.openShow(aShow) )
    
    def openShow(self,aShow):
        window = ShowWindow(self.widget,aShow)


class ShowWindow():
    def __init__(self,master, aShow):
        show = aShow
        self.widget = tk.Toplevel(master, padx=150, pady=50)
        title = "Opciones para: " + show.title()
        self.widget.title(title)
        ratingDateLabel = tk.Label(self.widget, text="Fecha de Rating (Formato DD/MM/AAAA)")
        ratingDateLabel.pack()
        ratingDate = tk.Entry(self.widget, bd=2)
        ratingDate.insert(0,"11/11/2011")
        ratingDate.pack()
        ratingButton = tk.Button(self.widget, text="VER RATING",
                                 command=lambda: self.createRatingWindow(show,ratingDate))
        ratingButton.pack(side=tk.TOP)
        popularityStartDateLabel = tk.Label(self.widget, text="Popularidad desde (Formato DD/MM/AAAA)")
        popularityStartDateLabel.pack()
        popularityStartDate = tk.Entry(self.widget, bd=2)
        popularityStartDate.pack()
        popularityEndDateLabel = tk.Label(self.widget, text="Hasta (Formato DD/MM/AAAA)")
        popularityEndDateLabel.pack()
        popularityEndDate = tk.Entry(self.widget, bd=2)
        popularityEndDate.pack()
        popularityButton = tk.Button(self.widget, text="VER POPULARIDAD")
        popularityButton.pack(side=tk.BOTTOM)

    def createRatingWindow(self, show, ratingDate):
        askedDate = datetime.datetime.strptime(ratingDate.get(), '%d/%m/%Y').date()
        window = RatingWindow(self.widget,show, askedDate)

class RatingWindow():
    def __init__(self,master, aShow, aDate):
        show = aShow
        widget = tk.Toplevel(master, padx=150, pady=50)
        title = "Rating para: " + show.title() + " en fecha " + aDate.strftime("%d/%m/%Y")
        widget.title(title)
        
        rating = tk.StringVar()
        ratingDisplay = tk.Label( widget,textvariable=rating,
                               font=("Ubuntu",40), relief=tk.RAISED )

        rating.set("42")
        ratingDisplay.pack()
        seePostsButton = tk.Button(widget, text="VER TWEETS",
                                 command=lambda: PostWindow(widget,aShow,myPostList))###
        seePostsButton.pack()

class PostWindow():
    def __init__(self,master, aShow, aPostList):
        show = aShow
        self.postList = aPostList
        self.widget = tk.Toplevel(master, padx=60, pady=10)
        title = "Lista de tweets de: " + show.title()
        self.widget.title(title)
        self.postViews = []
        
        self.positive = tk.IntVar()
        self.negative = tk.IntVar()
        self.neutral = tk.IntVar()
        self.createSentimentOptions(self.positive, self.negative, self.neutral)
        positive = 1
        resetPostsButton = tk.Button(self.widget, text="BUSCAR TWEETS",
                                     command=lambda:self.generatePosts())
        resetPostsButton.pack()
        
        self.generatePosts()

    def generatePosts(self):
        for view in self.postViews: view.widget.destroy()
        self.postViews = []
        for post in self.postList:
            if (post.sentiment()==1 and self.positive.get())  \
               or (post.sentiment()==-1 and self.negative.get()) \
               or (post.sentiment()==0 and self.neutral.get()):
                self.postViews.append(PostDisplay(self.widget, post))


    def createSentimentOptions(self, positive, negative, neutral):
        frame = tk.LabelFrame(self.widget, text="Filtro de tweets")
        frame.pack()
        positiveCheck = SentimentOption(frame,"Positivos", positive)
        negativeCheck = SentimentOption(frame,"Negativos", negative)
        neutralCheck = SentimentOption(frame,"Neutrales", neutral)
        positiveCheck.widget.grid(column=0,row=0) 
        negativeCheck.widget.grid(column=1,row=0)  
        neutralCheck.widget.grid(column=2,row=0)


class SentimentOption():
    def __init__(self,master, aName, aVariable):
        self.widget = tk.Checkbutton(master, text = aName, variable = aVariable,
                             onvalue = 1, offvalue = 0, height=5, 
                             width = 8)
        
class PostDisplay():
    def __init__(self,master,aPost):
        self.widget = tk.LabelFrame(master, text=aPost.author())
        self.widget.pack()
        content = tk.Label(self.widget, text=aPost.content(), wraplength=300)
        content.pack()





root = tk.Tk()
app = Application(master=root)
app.mainloop()

