# -*- coding: utf-8 -*-

import tkinter as tk
import datetime
from PostsView import *

class PostsWindow(tk.Toplevel):
    def __init__(self,master, aShow, aPostsView):
        show = aShow
        super().__init__(master, padx=60, pady=10)
        title = "Lista de tweets de: " + show.getName()
        self.title(title)
        self.postViews = []
        
        self.positive = tk.IntVar()
        self.negative = tk.IntVar()
        self.neutral = tk.IntVar()
        self.createSentimentOptions(self.positive, self.negative, self.neutral)
        self.positive.set(1)

        resetPostsButton = tk.Button(self, text="BUSCAR TWEETS")
        resetPostsButton.pack(side=tk.TOP)
        
        frame = tk.Frame(self, width=600, height=600)
        frame.pack(side=tk.BOTTOM)#, fill=tk.BOTH, expand=tk.TRUE)
        frame.grid_propagate(tk.FALSE)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        
        textArea = tk.Text(frame, borderwidth=3, relief="sunken")
        textArea.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
        
        scrollbar = tk.Scrollbar(frame, command=textArea.yview)
        scrollbar.grid(row=0, column=1, sticky='nsew')
        textArea['yscrollcommand'] = scrollbar.set
        
        resetPostsButton.config(command=lambda:self.generatePosts(textArea, aPostsView))
        
        self.generatePosts(textArea, aPostsView)

    def generatePosts(self, textArea, aPostsView):
        #for view in self.postViews: view.destroy()
        #self.postViews = [] 
        textArea.delete(1.0, tk.END)
        
        for post in aPostsView.getPosts():
            if (post.sentiment()==1 and self.positive.get())  \
               or (post.sentiment()==-1 and self.negative.get()) \
               or (post.sentiment()==0 and self.neutral.get()):
                self.displayPost(textArea, post)
                
    def displayPost(self, textArea, aPost):
        
        _date = aPost.date().strftime("%d/%m/%Y")
        _sentiment = aPost.sentiment()
        _author = aPost.author()
        _content = aPost.content()
        
        for data in [_date,_sentiment,_author,_content]:
            textArea.insert(tk.INSERT, str(data) + "\n\n")
        textArea.insert(tk.INSERT,"\n\n")


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
        
        

#Clase vieja de display de posts, ahora lo hago de otra forma
'''
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
'''
