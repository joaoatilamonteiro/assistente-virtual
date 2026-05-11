---
title: Jarvis - Assistente Virtual em Python
description: Assistente virtual inteligente com reconhecimento de voz e integração com Spotify.
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

* **`cabeca.py`**: O cérebro do assistente. Contém o loop principal que interpreta os comandos recebidos.
* **`boca.py`**: Gerencia a saída de áudio e as saudações personalizadas baseadas no horário do dia.
* **`ouvido.py`**: Configuração do microfone e motor de transcrição de voz para texto.
* **`spotify_client.py`**: Uma biblioteca (wrapper) personalizada que simplifica as requisições para a API do Spotify, tratando inclusive limites de requisição (Rate Limit).
* **`login.py`**: Gerencia as credenciais e o processo de login para garantir que o assistente tenha permissão de acesso.
* **`spotify_falado.py`**: Módulo de interface que permite escolher em qual dispositivo o áudio deve ser reproduzido.

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
