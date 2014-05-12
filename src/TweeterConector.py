class TweeterConector(list):

    def __init__(self, tweetsList):
        list.__init__([])
        """ En tweets van los tweets harcodeados para probar """
        tweets = []
        self.extend(tweetsList)

    def tweetsBasicRequest(initialDate, finalDate, hashtags):
        print ("TODO: TweeterConector::tweetsInPeriod(initialDate, finalDate)")
        return []
