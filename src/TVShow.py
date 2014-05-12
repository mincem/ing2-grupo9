class TVShow:

    def __init__(self, title, hashtags, days, time):
        self._title = title
        self._hashtags = hashtags
        self._days = days
        self._time = time

    def getHashtags(self):
        return self._hashtags

    def getDays(self):
        return self._days

    def getTime(self):
        return self._time

    def getTitle(self):
        return self._title

class MyTVShows:

    def __init__(self, shows):
        self._shows = shows

    def getShows(self):
        return _shows

class BailandoTVShow(TVShow):

    def __init__(self):
        hashtags = ["Bailando2014, cuervoTinelli, #Showmatch2014"]
        days = ["lunes"]
        time = "22:30"
        super(BailandoTVShow, self).__init__("Bailando por un sueño", 
                       hashtags,
                       days, time)

class Seis78TVShow(TVShow):

    def __init__(self):
        hashtags = ["678elprograma", "678", 
                    "periodismo militante"]
        days = ["lunes"]
        time = "21:30"
        super(Seis78TVShow, self).__init__("678", 
                       hashtags,
                       days, time)
