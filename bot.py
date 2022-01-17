import tweepy, sys
from decouple import config
import datetime as dt

client = tweepy.Client(
    consumer_key= config('API_KEY'),
    consumer_secret= config('API_KEY_SECRET'),
    access_token= config('ACCESS_KEY'),
    access_token_secret= config('ACCESS_TOKEN_SECRET')
)

hours = dt.datetime.now().hour
minutes = dt.datetime.now().minute
day = dt.datetime.now().day
month = dt.datetime.now().month
response = "Test skipped"

reminder_stream  = f"🎵 | Lembrete - STREAM ({day}/{month})\n\nONCEs, passem no nosso carrd e façam sua stream diária no Spotify usando nossas playlists de metas e, também, no Youtube usando a lista de vídeos que está nesse carrd.\n\nDeixem um 🆗 aqui e  um RT se estiverem fazendo stream!\nhttps://lembretestream.carrd.co/"
reminder_voting  = f"🗳 | Lembrete - VOTAÇÃO ({day}/{month})\n\nONCEs, entrem no carrd e deixem seus votos nas votações indicadas, elas são bem rápidas de participar!\n\nDeixem um🆗aqui e um RT se tiverem votado nelas e participem também dos nossos outros mutirões!\nhttps://lembretesparaonces.carrd.co/#votacoes"
reminder_collect = f"🔔 | Lembrete - COLETA({day}/{month})\n\nONCEs, entrem no carrd e coletem para as votações indicadas, deixamos uma sugestão de quanto seria recomendado em cada app e tutoriais!\n\nDeixem um🆗aqui e um RT se tiverem coletado e participem também dos nossos mutirões!\nhttps://lembretesparaonces.carrd.co/#coleta"
reminder_forms   = f"📩 | Lembrete - VAGAS ({day}/{month})\n\nNós, da acordaonce, estamos abrindo vagas para adm. Quem estiver interessado e puder, se inscreva até o dia 19/02!\n\nPrós: diversão\nContras: sem salário\n\nObs: Não mude o user caso estiver inscrito.\n🔗Link do formulário:\nhttps://forms.gle/7wDHsJwFyPSHpu617"

url = 'https://api.twitter.com/2/tweets'

# Reminder voting: 11:00h BRT
if(hours == 14 and minutes < 10):
    response = client.create_tweet( text=reminder_voting )
# Reminder collect: 14:00h BRT
elif(hours == 17 and minutes < 10):
    response = client.create_tweet( text=reminder_collect )
# Reminder forms: 17:45h BRT
elif(hours == 20 and minutes >= 40 and minutes < 50):
    response = client.create_tweet( text=reminder_forms )
# Reminder stream: 18:00h BRT
elif(hours == 21 and minutes < 10):
    response = client.create_tweet( text=reminder_stream )

print(response)
