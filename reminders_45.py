from api_lib import new_tweet
import datetime as dt

hours = dt.datetime.now().hour
day = dt.datetime.now().day
month = dt.datetime.now().month

reminder_forms = f"📩 | Lembrete - VAGAS ({day}/{month})\n\nNós, da acordaonce, estamos abrindo vagas para adm. Quem estiver interessado e puder, se inscreva até o dia 19/02!\n\nPrós: diversão\nContras: sem salário\n\nObs: Não mude o user caso estiver inscrito.\n🔗Link do formulário:\nhttps://forms.gle/7wDHsJwFyPSHpu617"

response = "Log: Test skipped"

# Reminder forms: 17:45h BRT
if(hours == 20):
    response = new_tweet(reminder_forms)

print(response)