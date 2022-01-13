import tweepy, sys
from decouple import config
import datetime as dt

## Consts
CONSUMER_KEY = config('API_KEY')
CONSUMER_SECRET = config('API_KEY_SECRET')
ACCESS_KEY = config('ACCESS_KEY')
ACCESS_SECRET = config('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = config('BEARER_TOKEN')

reminder_stream  = "🎵 | Lembrete de STREAM\n\nONCEs, passem no nosso carrd e façam sua stream diária no Spotify usando nossas playlists de metas e, também, no Youtube usando a lista de vídeos que também está nesse carrd.\n\nDeixem um 🆗 aqui e  um RT se estiverem fazendo stream!\nhttps://lembretestream.carrd.co/ "
reminder_voting  = "🗳 | Lembrete de VOTAÇÃO\n\nONCEs, entrem no carrd e deixem seus votos nas votações indicadas, elas são bem rápidas de participar!\n\nDeixem um🆗aqui e um RT se tiverem votado nelas e participem também dos nossos outros mutirões!\nhttps://lembretesparaonces.carrd.co/#votacoes"
reminder_collect = "🔔 | Lembrete de COLETA\n\nONCEs, entrem no carrd e coletem para as votações indicadas, deixamos uma sugestão de quanto seria recomendado em cada app e tutoriais!\n\nDeixem um🆗aqui e um RT se tiverem coletado e participem também dos nossos mutirões!\nhttps://lembretesparaonces.carrd.co/#coleta"

hours = dt.datetime.now().hour

url = 'https://api.twitter.com/2/tweets'

client = tweepy.Client(
    consumer_key=config('API_KEY'),
    consumer_secret=config('API_KEY_SECRET'),
    access_token=config('ACCESS_KEY'),
    access_token_secret=config('ACCESS_TOKEN_SECRET')
)

if(hours == 13):
    response = client.create_tweet( text=reminder_stream  )
if(hours == 19):
    response = client.create_tweet( text=reminder_voting  )
if(hours == 21):
    response = client.create_tweet( text=reminder_collect )