import time

from pyautogui import hotkey, press
from art import tprint
from boca import nome, bemvindo, quemsoueu,falar
from ouvido import escuta
import os
from login import login
from spotify_falado import tocando_musica

tprint("Inicializado", font="basic")
cliente = login()
nome()
usuario = escuta()
bemvindo(usuario)

while True:
    comando = escuta()
    print(comando)

    if "cabeça página inicial" in comando:
        hotkey("winleft", "d")


    elif "cabeça" in comando and "música" in comando:
        os.system("spotify")
        falar(f"Qual música voce quer que eu toque?")

        nome_da_musica = escuta()
        if nome_da_musica:
            tocando_musica(cliente, nome_da_musica)


    elif "quem é você?" in comando:
        quemsoueu()

    elif "cabeça desligar" in comando:
        quit()





