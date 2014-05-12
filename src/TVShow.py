class TVShow:

    def __init__(self, title, hashtags, days, time):
        self._title = title
        self._hashtags = hashtags
        self._days = days
        self._time = time

    def getHashtags(self):
        return _hashtags

    def getDays(self):
        return _days

    def getTime(self):
        return _time

class MyTVShows:

    def __init__(self, shows):
        self._shows = shows

    def getShows(self):
        return _shows

class BailandoTVShow(TVShow):

    def __init__(self):
        hastags = ["#Bailando2014, cuervoTinelli, #Showmatch2014"]
        days = ["lunes"]
        time = "22:30"
        super.__init__(self,"Bailando por un sueño", 
                       hashtags,
                       days, time)

class 678TVShow(TVShow):

    def __init__(self):
        hastags = ["#678", "periodismo militante"]
        days = ["lunes"]
        time = "22:30"
        super.__init__(self, "678", 
                       hashtags,
                       days, time)
