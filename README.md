---
Jarvis - Assistente Virtual em Python
Assistente virtual inteligente com reconhecimento de voz e integração com Spotify.
---

## 🚀 Funcionalidades

* **Processamento de Voz Local:** Utiliza o modelo Vosk para reconhecimento de fala em português (PT-BR) sem necessidade de internet constante.
* **Síntese de Voz (TTS):** Respostas auditivas dinâmicas utilizando a biblioteca `pyttsx3`.
* **Integração Robusta com Spotify:**
* Fluxo de autenticação OAuth com servidor local para captura automática de token.
* Busca e reprodução de faixas e artistas.
* Seleção dinâmica de dispositivos ativos (celular, computador, Echo Dot, etc.).
* Controles de player (Pausar, Próxima, Anterior).


* **Automação de Sistema:** Comandos para gerenciar janelas e abrir aplicativos nativos.

## 📂 Estrutura do Projeto

O projeto é modularizado em diretórios lógicos para facilitar a manutenção e escalabilidade:

* **`/entendimento`**: Módulos centrais de processamento e interação com o usuário.
  * `cabeca.py`: O cérebro do assistente. Contém o loop principal que orquestra e interpreta os comandos.
  * `boca.py`: Gerencia a saída de áudio e as saudações personalizadas baseadas no horário do dia.
  * `ouvido.py`: Configuração de entrada de comandos de texto/voz para interação com a IA.
  * `login.py`: Gerencia as credenciais e o processo de login para garantir as permissões de acesso.

* **`/musica`**: Módulos dedicados à integração com serviços de mídia.
  * `spotify_client.py`: Wrapper personalizado que simplifica as requisições para a API do Spotify, tratando limites de requisição (Rate Limit).
  * `spotify_falado.py`: Módulo de interface que permite a escolha e o roteamento de áudio para os dispositivos disponíveis.

* **Arquivos Raiz**:
  * `informacoes.json`: (Não versionado) Contém as chaves de API privadas.
  * `como_o_spotify_decide_a_seed_das_musicas.txt`: Documentação sobre o funcionamento do algoritmo.
## 🛠️ Pré-requisitos

* Python 3.x
* Modelo Vosk (PT-BR) extraído na pasta `vosk_models/`.
* Conta de Desenvolvedor no Spotify (para obter `id_client` e `id_client_secret`).

## ⚙️ Configuração

Crie um arquivo `informacoes.json` na raiz do projeto com o seguinte formato:

```json
{
    "id_client": "SEU_CLIENT_ID",
    "id_client_secret": "SEU_CLIENT_SECRET",
    "url_redirecionamento": "http://127.0.0.1:8888/callback"
}

```

---
