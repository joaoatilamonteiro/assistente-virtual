from pyautogui import hotkey
from art import tprint
from boca import nome, bemvindo, quemsoueu,falar
from ouvido import escuta
import os
from login import login
from musica.spotify_client import controle_player
from musica.spotify_falado import tocando_musica


tprint("Inicializado", font="basic")
cliente = login()
controle = controle_player(cliente)
nome()
usuario = escuta()
bemvindo(usuario)

while True:
    comando = escuta()
    print(comando)

    if "cabeça página inicial" in comando:
        hotkey("winleft", "d")


    elif "cabeça" in comando and "música" in comando and "página inicial" in comando:
        os.system("spotify")
        falar(f"Qual música você quer que eu toque?")

        nome_da_musica = escuta()
        if nome_da_musica:
            tocando_musica(cliente, nome_da_musica)

        hotkey("win","d")

    elif "cabeça" in comando and "pausa" in comando or "parar" in comando and "música" in comando:
        falar("pausando a música...")
        controle.pausar()

    elif "cabeça" in comando and "despausa" in comando or "voltar" in comando and "música" in comando:
        falar("despausando a música...")
        controle.resume()

    elif "cabeça" in comando and "próxima" in comando and "música" in comando:
        falar("pausando a música...")
        controle.proxima_musica()


    elif "cabeça" in comando and "anterior" in comando and "música" in comando:
        falar("Indo para a música...")
        controle.musica_anterior()



    elif "quem é você" in comando:
        quemsoueu()

    elif "cabeça desligar" in comando:
        quit()





