import typer
from rich import print
from importlib.metadata import version as get_version
from bdh_linux.commands import install, setup, remove,tamizhi_lib

app = typer.Typer(
    name="bdh-linux",
    help="⚡ BDH Linux — Backend Developer OS setup tool",
)

app.add_typer(install.app, name="install")
app.add_typer(setup.app, name="setup")
app.add_typer(remove.app, name="remove")
app.add_typer(tamizhi_lib.app, name="tamizhi")
@app.command()
def version():
    """Show BDH Linux version"""
    v = get_version("bdh-linux")
    print(f"[cyan]⚡ bdh-linux v{v}[/cyan]")
    print("[green]Backend Developer OS — Arch/Manjaro[/green]")

@app.command()
def status():
    """Check what's installed"""
    import shutil
    tools = {
        "Python": "python",
        "FastAPI": "uvicorn",
        "PostgreSQL": "psql",
        "Docker": "docker",
        "Git": "git",
        "ZSH": "zsh",
        "bdh-fastapi-new": "bdh-fastapi-new",
    }
    print("\n[cyan]⚡ bdh-linux Status[/cyan]")
    print("=" * 30)
    for name, cmd in tools.items():
        if shutil.which(cmd):
            print(f"[green]✅ {name}[/green]")
        else:
            print(f"[red]❌ {name} — not installed[/red]")
    print("=" * 30)

@app.command()
def doctor():
    """Full system health check"""
    print("\n[cyan]⚡ bdh-linux Doctor[/cyan]")
    status()

if __name__ == "__main__":
    app()
