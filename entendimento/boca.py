import datetime
import pyttsx3


def falar(audio):
    texttospeech = pyttsx3.init()
    voice = texttospeech.getProperty("voices")
    texttospeech.setProperty("voice", voice[0].id)
    print(f"Texto para ser falado: {audio}")

    texttospeech.say(audio)
    texttospeech.runAndWait()


def tempo():
    hora_exata = f"agora são: {datetime.datetime.now().strftime('%H horas e %M minutos')}"
    data_exata = f"do dia: {datetime.datetime.now().strftime('%d do mês %m do ano %Y')}"

    return hora_exata, data_exata

def nome():
    falar(f"Qual seu nome?")


def quemsoueu():
    falar("sou um assistente virtual em desenvolvimento que busca lhe ajudar da melhor forma que conseguir")

def bemvindo(nome):
    hora_exata,data_exata = tempo()

    hora = datetime.datetime.now().hour
    if 6 <= hora < 12:
        falar(f"Olá {nome}, bom dia! {hora_exata}")

    elif 12 <= hora < 18:
        falar(f"Olá {nome}, boa tarde! {hora_exata}")

    elif 18 <= hora < 24:
        falar(f"Olá {nome}, boa noite! {hora_exata}")

    else:
        falar(f"Olá {nome}, boa madrugada!")


