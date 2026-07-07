import os
import urllib.request
from pathlib import Path
import typer
from rich import print

# Typer App-ஐ உருவாக்குகிறோம்
app = typer.Typer(help="📦 Tamizhi Package Manager")

LIBRARIES = {
    "http": {
        "name": "Tamizhi HTTP Web Server",
        "desc": "Native HTTP Server support for Tamizhi",
        "files": [
            {
                "url": "https://raw.githubusercontent.com/BackendDeveloperHub/Tamizhi/main/lib/http.tz",
                "dest": "~/.tamizhi/lib/http.tz"
            },
            {
                "url": "https://raw.githubusercontent.com/BackendDeveloperHub/Tamizhi/main/core/http_runtime.c",
                "dest": "~/.tamizhi/core/http_runtime.c"
            }
        ]
    }
}

def download_file(url, dest_path):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(dest_path, 'wb') as out_file:
        out_file.write(response.read())

@app.command("get")
def get_library(name: str = typer.Argument(None, help="Name of the library to install")):
    """Install a Tamizhi library (e.g., http)"""
    
    # யூசர் எந்த பெயரும் கொடுக்கவில்லை என்றால், லிஸ்ட்டைக் காட்ட வேண்டும்
    if not name:
        print("\n[bold cyan]📦 Available Tamizhi Libraries:[/bold cyan]")
        print("-" * 50)
        for key, info in LIBRARIES.items():
            print(f" 👉 [bold green][{key}][/bold green] : {info['name']} - {info['desc']}")
        print("-" * 50)
        print("Run [bold yellow]bdh-linux tamizhi get <library_name>[/bold yellow] to install.\n")
        return

    name = name.lower()
    
    # யூசர் கொடுத்த பெயர் இருந்தால் டவுன்லோட் செய்ய வேண்டும்
    if name in LIBRARIES:
        print(f"\n[bold yellow]⬇️ Installing '{name}' library...[/bold yellow]")
        for file_info in LIBRARIES[name]["files"]:
            dest = Path(file_info["dest"]).expanduser()
            dest.parent.mkdir(parents=True, exist_ok=True)
            
            print(f" 📥 Downloading {dest.name}...")
            try:
                download_file(file_info["url"], dest)
                print(f" [bold green]✅ Saved to {dest}[/bold green]")
            except Exception as e:
                print(f" [bold red]❌ Failed to download {dest.name}: {e}[/bold red]")
                return
                
        print(f"\n[bold green]🎉 Successfully installed {LIBRARIES[name]['name']}![/bold green]\n")
    else:
        print(f"[bold red]❌ Invalid library name '{name}'. Run without arguments to see the list.[/bold red]")
