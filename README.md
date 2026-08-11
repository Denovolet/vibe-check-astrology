# vibe-check-astrology

Script simples em Python que pega o horóscopo do dia via API, calcula uma pontuação de "vibe" e sugere algumas músicas da Apple Music.

## O que o projeto faz
- Consulta horóscopo diário
- Gera um Vibe Score
- Busca recomendações de músicas no iTunes/Apple Music
- Exibe o resultado formatado no terminal usando a lib `rich`

## Requisitos
- Python 3.10+
- Bibliotecas listadas no `requirements.txt`

## Como rodar
Clone o repositório e instale as dependências:

```bash
git clone [https://github.com/Denovolet/vibe-check-astrology.git](https://github.com/Denovolet/vibe-check-astrology.git)
cd vibe-check-astrology
pip install -r requirements.txt
python main.py