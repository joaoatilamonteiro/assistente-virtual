from ouvido import escuta
from boca import falar

def converter_texto(texto):
    dicionario = {"zero":0,
                   "um":1,
                  "dois":2,
                  "três":3,
                  "quatro":4
                  }

    palavra = str(texto).lower().strip()

    if palavra in dicionario:
        return dicionario[palavra]

    elif palavra.isdigit():
        return int(palavra)

    else:
        return None


def tocando_musica(client,musica):
    # 4. O seu bloco de teste entra aqui
    dispositivos = client.lista_dispositivos()

    if isinstance(dispositivos, list) and len(dispositivos) > 0:
        falar("escolha o dispositivo ")
        escolha = escuta()

        indice = converter_texto(escolha)
        if indice is not None:
            try:
                id_escolhido = dispositivos[indice]["id"]
                nome_escolhido = dispositivos[indice]["name"]
                falar(f"direcionando audio para {nome_escolhido}")

                falar(f"tocando {musica}")
                client.search_track(query = musica,device_id=id_escolhido)

            except IndexError:
                falar(f"Desculpe, o número {indice} não está na lista de aparelhos.")
        else:
            falar("Comando invalido")
    else:
        falar("Nenhum dispositivo disponivel")
