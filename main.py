import random
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

SIGNOS = {
    "1": ("aries", "Áries ♈"),
    "2": ("taurus", "Touro ♉"),
    "3": ("gemini", "Gêmeos ♊"),
    "4": ("cancer", "Câncer ♋"),
    "5": ("leo", "Leão ♌"),
    "6": ("virgo", "Virgem ♍"),
    "7": ("libra", "Libra ♎"),
    "8": ("scorpio", "Escorpião ♏"),
    "9": ("sagittarius", "Sagitário ♐"),
    "10": ("capricorn", "Capricórnio ♑"),
    "11": ("aquarius", "Aquário ♒"),
    "12": ("pisces", "Peixes ♓"),
}


def buscar_horoscopo(signo: str):
    url = f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={signo}&day=TODAY"
    try:
        res = requests.get(url, timeout=6)
        if res.status_code == 200:
            dados = res.json()
            if dados.get("success"):
                return dados["data"]["horoscope_data"]
    except requests.RequestException:
        pass

    return (
        "Hoje o universo pede para você brilhar, beber água e focar no seu sucesso. "
        "Sua energia está super alta e nada pode apagar seu brilho! ✨"
    )


def buscar_musicas_vibe(termo_busca: str):
    url = f"https://itunes.apple.com/search?term={termo_busca}&entity=song&limit=4"
    try:
        res = requests.get(url, timeout=6)
        if res.status_code == 200:
            resultados = res.json().get("results", [])
            playlist = []
            for item in resultados:
                playlist.append(
                    {
                        "track": item.get("trackName"),
                        "artist": item.get("artistName"),
                    }
                )
            if playlist:
                return playlist
    except requests.RequestException:
        pass

    return [
        {"track": "Espresso", "artist": "Sabrina Carpenter"},
        {"track": "Cruel Summer", "artist": "Taylor Swift"},
        {"track": "Good 4 U", "artist": "Olivia Rodrigo"},
        {"track": "PINK!", "artist": "Chappell Roan"},
    ]


def gerar_vibe_score():
    vibes = [
        "Main Character Energy 💅✨",
        "Cozy & Soft Girl 🎀🕯️",
        "Sassy & Unstoppable 🔥💋",
        "Manifesting Success 💅💸",
        "Dramatic & Cute 🩰🌸",
    ]
    return random.choice(vibes)


if __name__ == "__main__":
    console.print(
        Panel(
            "[bold hot_pink]✨ VIBE CHECK & ASTROLOGY DAILY CLI ✨[/bold hot_pink]\n"
            "[dim pink1]Descubra o astral do seu signo & receba a playlist pro seu dia[/dim pink1]",
            border_style="magenta",
            expand=False,
        )
    )

    console.print("\n[bold pink1]Qual é o seu signo, gatinha?[/bold pink1]")
    for key, (_, nome) in SIGNOS.items():
        console.print(f"[bold magenta]{key}.[/bold magenta] {nome}")

    opcao = console.input("\n[bold hot_pink]Escolha o número (1-12): [/bold hot_pink]").strip()

    if opcao in SIGNOS:
        signo_key, signo_nome = SIGNOS[opcao]
    else:
        signo_key, signo_nome = "leo", "Leão ♌ (Default Queen)"

    console.print(f"\n[bold yellow]Consultando as estrelas para {signo_nome}... 🔮[/bold yellow]\n")

    horoscopo = buscar_horoscopo(signo_key)
    vibe_hoje = gerar_vibe_score()

    console.print(
        Panel(
            f"[bold white]{horoscopo}[/bold white]\n\n"
            f"✨ [bold hot_pink]Vibe do Dia:[/bold hot_pink] [bold cyan]{vibe_hoje}[/bold cyan]\n"
            f"💄 [bold hot_pink]Dica Aesthetic:[/bold hot_pink] Coloque seu acessório favorito e arrase!",
            title=f"🌸 Horóscopo de Hoje - {signo_nome} 🌸",
            border_style="hot_pink",
        )
    )

    console.print("\n[bold hot_pink]🎵 Gerando sua Playlist 'Main Character' via Apple Music API...[/bold hot_pink]\n")

    termos_busca = ["sabrina carpenter", "taylor swift", "chappell roan", "pop party"]
    playlist = buscar_musicas_vibe(random.choice(termos_busca))

    tabela = Table(
        title="[bold magenta]🎧 Your Daily Vibe Playlist[/bold magenta]",
        border_style="magenta",
        header_style="bold hot_pink",
    )
    tabela.add_column("Música", style="bold white")
    tabela.add_column("Artista", style="cyan")

    for m in playlist:
        tabela.add_row(m["track"], m["artist"])

    console.print(tabela)
    console.print("\n[bold hot_pink]Pronta pra dominar o dia! ✨💅[/bold hot_pink]\n")