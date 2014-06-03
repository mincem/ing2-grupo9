# -*- coding: utf-8 -*-

import tkinter as tk
import datetime
import time
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
        aFilter = []
        textArea.delete(1.0, tk.END)
        
        if self.positive.get():
            aFilter.append('Positivo')
        if self.negative.get():
            aFilter.append('Negativo')
        if self.neutral.get():
            aFilter.append('Neutro')

        aPostsView.setSentimentFilter(aFilter)
        for post in aPostsView.getPosts():
            self.displayPost(textArea, post)
                
    def displayPost(self, textArea, aPost):
        
        _date = aPost.getDateTime()
        _sentiment = aPost.getSentiment()
        _author = aPost.getAuthor()
        _content = aPost.getContent()

        _dateString = "Fecha: " + time.strftime('%d/%m/%Y %H:%M:%S', _date)
        _sentimentString = "\t Calificación: " + str(_sentiment) + "\n"
        _authorString = "Autor: " + str(_author) + "\n"
        _contentString = str(_content) + "\n\n"

        
        for data in [_dateString,_sentimentString,_authorString,_contentString]:
            try: textArea.insert(tk.INSERT, data)
            except tk.TclError:
                isValidForTk = lambda character: ord(character) <= 2000
                cleanData = ''.join(filter(isValidForTk, data))
                textArea.insert(tk.INSERT, cleanData)
                    

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
        
        
