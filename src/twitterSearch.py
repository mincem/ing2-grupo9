__author__ = 'Nick'
#Se puede bajar en zip de aca la libreria https://github.com/ryanmcgrath/twython
#luego van a la carpeta y hacen install con el setup
#importo la libreria
from twython import Twython, TwythonError

#Aca se instancia y se loguea, las claves con mias, funcan, va hardcodeado
APP_KEY = 'D0PYmI7UMWHyzISn4Z7hPx8Mc'
APP_SECRET = 'NNPnwOereOGZhzDxYrRrgM7IvU8khzSW5zT4F2F8LKs5yBwJz1'

twitter = Twython(APP_KEY,APP_SECRET)

auth = twitter.get_authentication_tokens()

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

#Esto no se si es necesario
twitterFinal = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

#Armo la query, aca esta la pagina para ver que parametros y que palabras claves 
#usar para la query de un search: https://dev.twitter.com/docs/using-search
keyword = 'casla' #palabra a buscar
hasta = '2014-05-10'
query = keyword + ' until:' + hasta
#desde = '2014-05-09'
#query = keyword + ' since:' + desde + + ' until:' + hasta 

#Aca hago el search, en search results se guardan los objetos 'tweets'
#Se podrian guardar los tweets en algun archivo o algo asi
try:
    search_results = twitter.search(q=query, count=50)
except TwythonError as e:
    print(e)

#Aca hay mas detalles de los objetos 'tweet': https://dev.twitter.com/docs/platform-objects/tweets
#Lo que mas nos interesa:
#tweet['text'].encode('utf-8')
#tweet['created_at']
#tweet['coordinates']
	
#Esto lo imprime
for tweet in search_results['statuses']:
    print ('Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'), tweet['created_at']))
    print (tweet['text'].encode('utf-8'), '\n')

#Puse esto para que no termine el programa
userInput = input('Give me a value')

