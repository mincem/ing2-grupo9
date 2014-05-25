import datetime
import time

class TVShow:

    def __init__(self, name, keywords, airingDays, startTime, endTime):
        self._name = name
        self._keywords = keywords
        self._airingDays = airingDays
        self._startTime = startTime
        self._endTime = endTime

    def getKeywords(self):
        return self._keywords

    def getEndTime(self):
        return self._endTime

    def getStartTime(self):
        return self._startTime

    def getName(self):
        return self._name

    def getAiringDays(self):
        return self._airingDays

class MyTVShows():

    def __init__(self, shows):
        self._shows = shows

    def getShows(self):
        return self._shows
    
    def len(self):
        return len(self.getShows())

class BailandoTVShow(TVShow):

    def __init__(self):
        keywords = ["Bailando2014", "cuervoTinelli", "#Showmatch2014"]
        airingDays = ["lunes"]
        startTime = datetime.time(22, 30)
        endTime = datetime.time(23, 59)
        super(BailandoTVShow, self).__init__("Bailando por un sueño", 
                                              keywords,
                                              airingDays, startTime, 
                                              endTime)

class Seis78TVShow(TVShow):

    def __init__(self):
        keywords = ["678elprograma", "678", 
                    "periodismo militante"]
        airingDays = ["lunes"]
        startTime = datetime.time(21, 00)
        endTime = datetime.time(22, 30)
        super(Seis78TVShow, self).__init__("678", 
                                           keywords,
                                           airingDays, startTime,
                                           endTime)
