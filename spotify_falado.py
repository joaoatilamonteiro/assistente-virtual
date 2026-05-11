import json
from ouvido import escuta
from boca import falar

def tocando_musica(client,musica):
    # 4. O seu bloco de teste entra aqui
    dispositivos = client.lista_dispositivos()

    if isinstance(dispositivos, list) and len(dispositivos) > 0:
        falar(input("escolha o dispositivo "))
        escolha = input("escolha o dispositivo ")

        try:
            indice = int(escolha)
            id_escolhido = dispositivos[indice]["id"]
            nome_escolhido = dispositivos[indice]["name"]
            print(f"direcionando audio para {nome_escolhido}")

            client.search_track(query = musica,device_id=id_escolhido)
        except (ValueError, IndexError):
            print("Opcao invalida")
    else:
        print("nenhum dispositivo disponivel para spotify")

