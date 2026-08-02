import json
from musica.spotify_client import auto_login, SCOPES, SpotifyClient


def login():
    # 1. Lemos o arquivo de configurações exatamente como no seu main.py
    with open("../informacoes.json", "r", encoding="utf-8") as file:
        dados = json.load(file)

    print("Iniciando login para o teste...")

    # 2. Executamos o fluxo de autenticação para pegar o token fresquinho
    token = auto_login(
        dados["id_client"],
        dados["id_client_secret"],
        dados["url_redirecionamento"],
        SCOPES
    )

    if not token:
        print("Falha ao obter o token. Verifique o login.")
        return

    # 3. Com o token em mãos, "ligamos" o Jarvis
    client = SpotifyClient(token)
    print("Login feito com sucesso!")
    return client



# Essa linha garante que o teste só rode se você executar este arquivo diretamente