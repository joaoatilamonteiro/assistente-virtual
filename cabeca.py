import time

from pyautogui import hotkey, press
from art import tprint
from boca import nome, bemvindo, quemsoueu,falar
from ouvido import escuta
import os
from login import login

tprint("Inicializado", font="basic")

nome()
comando = escuta()

print(comando)
bemvindo(comando)
while True:
    comando = escuta()
    print(comando)

    if "cabeça página inicial" in comando:
        hotkey("winleft", "d")


    elif "cabeça" in comando and "música" in comando and "página inicial" in comando:
        os.system("spotify")
        falar("Certo, em qual dispositivo?")
        #como faço aqui?
        #tenho que passar a funcao com a musica
        login(comando)






    elif "quem é você?" in comando:
        quemsoueu()

    elif "cabeça desligar" in comando:
        quit()





