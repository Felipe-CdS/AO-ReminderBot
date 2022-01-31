from api_lib import new_tweet
import datetime as dt

hours = dt.datetime.now().hour
day = dt.datetime.now().day
month = dt.datetime.now().month

reminder_stream  = f"🎵 | Lembrete - STREAM ({day}/{month})\n\nONCEs, passem no nosso carrd e façam sua stream diária no Spotify usando nossas playlists de metas e, também, no Youtube usando a lista de vídeos que está nesse carrd.\n\nDeixem um 🆗 aqui e  um RT se estiverem fazendo stream!\nhttps://lembretestream.carrd.co/"
reminder_voting  = f"🗳 | Lembrete - VOTAÇÃO ({day}/{month})\n\nONCEs, entrem no carrd e deixem seus votos nas votações indicadas, elas são bem rápidas de participar!\n\nDeixem um🆗aqui e um RT se tiverem votado nelas e participem também dos nossos outros mutirões!\nhttps://lembretesparaonces.carrd.co/#votacoes"
reminder_collect = f"🔔 | Lembrete - COLETA({day}/{month})\n\nONCEs, entrem no carrd e coletem para as votações indicadas, deixamos uma sugestão de quanto seria recomendado em cada app e tutoriais!\n\nDeixem um🆗aqui e um RT se tiverem coletado e participem também dos nossos mutirões!\nhttps://lembretesparaonces.carrd.co/#coleta"

response = "Log: Test skipped"

# Reminder voting: 11:00h BRT
if(hours == 13):
    response = new_tweet(reminder_voting)
# Reminder collect: 14:00h BRT
elif(hours == 17):
    response = new_tweet(reminder_collect)
# Reminder stream: 18:00h BRT
elif(hours == 21):
    response = new_tweet(reminder_stream)

print(response)
