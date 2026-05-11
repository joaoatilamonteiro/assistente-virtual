import datetime
import pyttsx3

texttospeech = pyttsx3.init()
voice = texttospeech.getProperty("voices")
texttospeech.setProperty("voice", voice[0].id)
def falar(audio):
    print(f"Jarvis diz: {audio}")  # <- coloquei isso para ver na tela!

    texttospeech.say(audio)
    texttospeech.runAndWait()


def tempo():
    hora_exata = f"agora são:{datetime.datetime.now().strftime('%H horas e %M minutos')}"
    data_exata = f"do dia:{datetime.datetime.now().strftime('%d do mês %m do ano %Y')}"

    return hora_exata, data_exata

def nome():
    falar(f"Qual seu nome?")

def qual_musica():
    falar(f"Qual música voce quer que eu toque?")

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


"C:\projects\python_projects\jarvis\vosk_models"
"como_o_spotify_decide_a_seed_das_musicas.txt"
"informacoes.json"