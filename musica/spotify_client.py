import time
import urllib.parse
import requests
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer


# Carrega configurações

SCOPES = ["playlist-read-private",
          "playlist-read-collaborative",
          "playlist-modify-private",
          "playlist-modify-public",
          "user-modify-playback-state",
          "user-read-playback-state"
          ]


def get_auth_url(client_id, redirect_uri, scopes):
    base_url = "https://accounts.spotify.com/authorize"
    scope_str = " ".join(scopes)

    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": scope_str,
        "show_dialog": "true"
    }

    return f"{base_url}?{urllib.parse.urlencode(params)}"


def exchange_code_for_token(code, client_id, client_secret, redirect_uri):
    url = "https://accounts.spotify.com/api/token"

    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("Token recebido com sucesso!")
        return response.json()["access_token"]
    else:
        print(f"Error loading token: {response.text}")
        return None


class SpotifyClient:
    def __init__(self, token):
        self.token = token
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def _make_request(self, method, url, **kwargs):
        while True:
            response = requests.request(method, url, headers=self.headers, **kwargs)

            # Tratamento de Rate Limit (Erro 429)
            if response.status_code == 429:
                retry_after = int(response.headers.get("Retry-After", 5))
                print(f"Rate limit reached. Waiting {retry_after} seconds...")
                time.sleep(retry_after + 1)
                continue

            return response

    def get_user_id(self):
        url = "https://api.spotify.com/v1/me"
        response = self._make_request("GET", url)

        if response.status_code == 200:
            return response.json()["id"]
        else:
            print(f"Error fetching profile: {response.status_code}")
            return None

    def lista_dispositivos(self):
        url = "https://api.spotify.com/v1/me/player/devices"

        response = self._make_request("GET",url)
        if response.status_code == 200:
            dispositivos = response.json().get("devices", [])
            if not dispositivos:
                return []
            for idx, dev in enumerate(dispositivos):
                status = "Sendo usado" if dev["is_active"] else "Disponivel"
                print(f"{idx} - {dev['name']} ({dev['type']}) - [{status}]")

            return dispositivos

        else:
            print(f"Error finding devices: {response.status_code}")

    def search_track(self, query, device_id=None):
        # 1. Busca a música
        url_search = "https://api.spotify.com/v1/search"
        params = {
            "q": query,
            "type": "track",
            "limit": 1
        }

        response = self._make_request("GET", url_search, params=params)

        if response.status_code == 200:
            items = response.json()["tracks"]["items"]
            if items:
                track_uri = items[0]["uri"]
                nome_musica = items[0]["name"]
                nome_artista = items[0]["artists"][0]["name"]
                print(f"[Jarvis] Localizei: {nome_musica} de {nome_artista}")

                # 2. Prepara o comando de reprodução
                url_play = "https://api.spotify.com/v1/me/player/play"

                if device_id:
                    url_play += f"?device_id={device_id}"

                # Enviamos apenas a URI da música encontrada em uma lista
                payload = {
                    "uris": [track_uri]
                }

                res_play = self._make_request("PUT", url_play, json=payload)

                # O código 204 significa que o Spotify aceitou o comando com sucesso
                if res_play.status_code == 204:
                    print(f"Reproduzindo '{nome_musica}' agora.")
                    return True
                else:
                    print(f"Erro ao dar play: {res_play.status_code}")
                    return False
            else:
                print(f"Não encontrei nenhuma música para: {query}")
                return False
        else:
            print(f"Erro na busca: {response.status_code}")
            return False

    def create_playlist(self, id_user, name_playlist, description):
        url_create_playlist = f"https://api.spotify.com/v1/users/{id_user}/playlists"

        payload = {
            "name": name_playlist,
            "description": description,
            "public": False
        }

        response = self._make_request("POST", url_create_playlist, json=payload)

        if response.status_code == 201:
            return response.json()["id"]
        else:
            print(f"Search error: {response.status_code}")
            return None

    def add_track_playlist(self, id_playlist, track_list):
        url = f"https://api.spotify.com/v1/playlists/{id_playlist}/tracks"

        size_track_list = len(track_list)
        for i in range(0, size_track_list, 100):
            pacote = track_list[i: i + 100]
            payload = {"uris": pacote}
            response = self._make_request("POST", url, json=payload)
            if response.status_code != 201:
                print(f"Search error: {response.status_code}")

    def procura_artista(self, artist_name,device_id = None):
        #o achou vai servir para verificar se a API achou ou nao o arista
        #o tocou vai servir para verificar se a API conseguiu tocar ou nao o artista
        url_search_artist = "https://api.spotify.com/v1/search"
        parametros = {"q": artist_name, "type": "artist", "limit": 1}
        response = self._make_request("GET", url_search_artist, params = parametros)

        if response.status_code == 200:
            items = response.json()["artists"]["items"]
            if items:
                artist_uri = items[0]["uri"]
                print(f"Localizei {items[0]["name"]}\nIniciando reprodução")

                url_play = "https://api.spotify.com/v1/me/player/play"

                if device_id:
                    url_play+= f"?device_id={device_id}"

                playload = {
                    "context_uri": artist_uri
                }

                res_play = self._make_request("PUT", url_play, json = playload)

                if res_play.status_code == 204:
                    print("Música tocando...")
                    achou = True
                    tocou = True
                    return achou, tocou

                else:
                    print(f"erro ao tocar {artist_name}\nerro:{res_play.status_code}")
                    achou = True
                    tocou = False
                    return achou, tocou

            else:
                print(f"Não foi achado o artista {artist_name}")

# Variável global para o servidor local
captured_code = None


class RequestHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return  # Silencia logs

    def do_GET(self):
        global captured_code
        if "/callback" in self.path:
            query = urllib.parse.urlparse(self.path).query
            query_components = urllib.parse.parse_qs(query)

            if "code" in query_components:
                captured_code = query_components["code"][0]
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"<h1>Success! You can close this tab.</h1>")
                self.wfile.write(b"<script>window.close();</script>")
            else:
                self.send_error(400, "Code not found")


def auto_login(client_id, client_secret, redirect_uri, scopes):
    global captured_code
    captured_code = None  # Reseta a variável por segurança

    link = get_auth_url(client_id, redirect_uri, scopes)

    print("Abrindo o navegador para login...")
    webbrowser.open(link)

    # Inicia servidor local para esperar a resposta
    server_address = ('127.0.0.1', 8888)
    httpd = HTTPServer(server_address, RequestHandler)

    print("Aguardando retorno do Spotify...")

    # O SEGREDO AQUI: O servidor só para de ouvir quando o código for capturado.
    # Isso ignora requisições de favicon ou fantasmas do navegador.
    while captured_code is None:
        httpd.handle_request()

    print("Código capturado via servidor automático!")

    # Agora sim, faz a troca pelo token
    return exchange_code_for_token(captured_code, client_id, client_secret, redirect_uri)

class controle_player:
    def __init__(self,spotify_client):
        self.client = spotify_client

    def pausar (self, device_id=None):
        url_pause = "https://api.spotify.com/v1/me/player/pause"
        if device_id:
            url_pause += f"?device_id={device_id}"
        res = self.client._make_request("PUT",url_pause)

        if res.status_code == 204 or 200:
            print("musica pausada")

        else:
            print(f"erro ao pausar a musica\n{res.status_code}")

    def resume (self, device_id=None):
        url_pause = "https://api.spotify.com/v1/me/player/play"
        if device_id:
            url_pause += f"?device_id={device_id}"
        res = self.client._make_request("PUT",url_pause)

        if res.status_code == 204 or 200:
            print("música voltando a tocar")

        else:
            print(f"erro ao voltar a musica\n{res.status_code}")

    def proxima_musica(self,device_id=None):

        url_next = "https://api.spotify.com/v1/me/player/next"

        if device_id:
            url_next += f"?device_id={device_id}"

        res = self.client._make_request("POST",url_next)

        if res.status_code == 204 or 200:
            print("Pulando para a proxima musica")
        else:
            print(f"erro ao avancar {res.status_code}")

    def musica_anterior(self,device_id = None):
        url_prev = "https://api.spotify.com/v1/me/player/previous"
        if device_id:
            url_prev += f"?device_id={device_id}"

        res = self.client._make_request("POST",url_prev)

        if res.status_code == 204 or 200:
            print("Voltando para a musica anterior")
        else:
            print(f"erro ao voltar {res.status_code}")


