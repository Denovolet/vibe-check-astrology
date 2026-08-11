
import random
import requests
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

SIGNS = [
    "aries", "taurus", "gemini", "cancer", 
    "leo", "virgo", "libra", "scorpio", 
    "sagittarius", "capricorn", "aquarius", "pisces"
]

def get_horoscope(sign):
    url = f"https://horoscope-app-api.vercel.app/api/v1/get-horoscope/daily?sign={sign}&day=TODAY"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            return res.json().get("data", {}).get("horoscope_data", "")
    except Exception:
        pass
    return "Dia neutro por aqui, aproveite o momento."

def get_tracks(query):
    url = f"https://itunes.apple.com/search?term={query}&entity=song&limit=3"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            results = res.json().get("results", [])
            return [(item.get("artistName"), item.get("trackName")) for item in results]
    except Exception:
        pass
    return [("Dua Lipa", "Levitating"), ("Taylor Swift", "Bejeweled")]

def main():
    console.clear()
    console.print(Panel("[bold magenta]VIBE CHECK DIÁRIO[/bold magenta]", expand=False))
    
    sign = input("\nDigite seu signo (em inglês, ex: gemini, leo): ").strip().lower()
    if sign not in SIGNS:
        sign = random.choice(SIGNS)
        console.print(f"[yellow]Signo não reconhecido. Usando {sign.capitalized()}...[/yellow]")

    console.print("\nConsultando APIs...")
    horoscope = get_horoscope(sign)
    score = random.randint(60, 100)
    tracks = get_tracks("pop energetic")

    console.print(f"\n[bold]Horóscopo:[/bold] {horoscope}\n")

    table = Table(title=f"Vibe Score: {score}%")
    table.add_column("Artista", style="cyan")
    table.add_column("Música", style="green")

    for artist, track in tracks:
        table.add_row(artist, track)

    console.print(table)
    console.print("\n[bold green]Pronto![/bold green]")

if __name__ == "__main__":
    main()