'''import typer
import subprocess
import os
from rich import print

app = typer.Typer(help="Setup bdh-linux components")

BASE_URL = "https://raw.githubusercontent.com/BackendDeveloperHub/bdh-linux/main"

def run(cmd: str):
    subprocess.run(cmd, shell=True)

@app.command()
def terminal():
    """Setup ZSH + BDH prompt + aliases"""
    print("[cyan]⚡ Setting up bdh-linux Terminal...[/cyan]")
    print("=" * 30)

    # Install ZSH
    print("[yellow]📦 Installing ZSH...[/yellow]")
    run("sudo pacman -S --noconfirm zsh git curl")

    # Oh My Zsh
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh")):
        print("[yellow]⚡ Installing Oh My Zsh...[/yellow]")
        run("git clone --depth=1 https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh")
    else:
        print("[yellow]⚡ Oh My Zsh already exists, skipping...[/yellow]")

    # Powerlevel10
    # Powerlevel10k
       
    # Powerlevel10k
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh/custom/themes/powerlevel10k")):
         run("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k")
    else:
         print("[yellow]⚡ Powerlevel10k already exists, skipping...[/yellow]")

# zsh-autosuggestions
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")):
         run("git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")
    else:
         print("[yellow]⚡ zsh-autosuggestions already exists, skipping...[/yellow]")

# zsh-syntax-highlighting
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")):
         run("git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")
    else:
         print("[yellow]⚡ zsh-syntax-highlighting already exists, skipping...[/yellow]")
     

    # Plugins
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")):
        run("git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")

    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")):
        run("git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")

    # BDH Configs — curl வழியா
    print("[yellow]🔧 Applying BDH configs...[/yellow]")
    run(f"curl -fsSL {BASE_URL}/configs/.zshrc -o ~/.zshrc")
    run(f"curl -fsSL {BASE_URL}/configs/aliases.sh -o ~/.aliases.sh")

    # Shell மாத்த
    run("sudo usermod -s /bin/zsh $USER")

    print("")
    print("[green]✅ Terminal setup done![/green]")
    print("[green]💡 Run 'p10k configure' to customize prompt![/green]")
    print("[green]⚡ Restart terminal to apply![/green]")
    print('reset') 

@app.command()
def packages():
    """Install all BDH packages"""
    print("[cyan]⚡ Setting up BDH Packages...[/cyan]")
    print("=" * 30)
    run(f"curl -fsSL {BASE_URL}/scripts/install-packages.sh -o /tmp/install-packages.sh")
    run("bash /tmp/install-packages.sh")
    print("")
    print("[green]✅ Packages setup done![/green]")

@app.command()
def git():
    """Setup Git global config"""
    print("[cyan]⚡ Setting up Git...[/cyan]")
    print("=" * 30)
    name = typer.prompt("Your name")
    email = typer.prompt("Your email")
    run(f'git config --global user.name "{name}"')
    run(f'git config --global user.email "{email}"')
    run("git config --global init.defaultBranch main")
    print("")
    print("[green]✅ Git setup done![/green]")

@app.command()
def docker():
    """Install and setup Docker"""
    print("[cyan]⚡ Setting up Docker...[/cyan]")
    print("=" * 30)
    run("sudo pacman -S --noconfirm docker docker-compose")
    run("sudo systemctl enable docker")
    run("sudo systemctl start docker")
    run("sudo usermod -aG docker $USER")
    print("")
    print("[green]✅ Docker setup done![/green]")
'''

import typer
import subprocess
import os
from rich import print

app = typer.Typer(help="Setup bdh-linux components")

BASE_URL = "https://raw.githubusercontent.com/BackendDeveloperHub/bdh-linux/main"

def run(cmd: str):
    subprocess.run(cmd, shell=True)

# --- Puthiya Network Command Inga ---

@app.command()
def network():
    """Scan and Connect to Wi-Fi (Arch Linux)"""
    print("[cyan]📡 BDH-Linux Network Link aarambikkuthu...[/cyan]")
    print("=" * 30)

    # NetworkManager active-ah irukkannu check pannurom
    print("[yellow]🔍 Checking NetworkManager status...[/yellow]")
    run("sudo systemctl enable --now NetworkManager")

    # Wi-Fi Scan
    print("[yellow]🔭 Scanning for available networks...[/yellow]")
    run("nmcli device wifi rescan")
    # Scan results-ah terminal-la kaaturoom
    run("nmcli -f SSID,BARS,SECURITY device wifi list")

    print("-" * 30)
    ssid = typer.prompt("Select panna Wi-Fi Name (SSID)")
    password = typer.prompt("Wi-Fi Password", hide_input=True)

    print(f"[yellow]⚡ Connecting to {ssid}...[/yellow]")
    # nmcli moolama connect pandroom
    result = subprocess.run(f'nmcli device wifi connect "{ssid}" password "{password}"', shell=True)

    if result.returncode == 0:
        print(f"[green]✅ Successfully connected to {ssid}![/green]")
        print("[cyan]🌐 Testing connection...[/cyan]")
        run("ping -c 3 google.com")
    else:
        print("[red]❌ Connection fail aayiduchi! Password check pannunga.[/red]")

# --- Unga pazhaya commands (terminal, packages, git, etc.) ellam appadiyae thodarum ---
@app.command()
def terminal():
    """Setup ZSH + BDH prompt + aliases"""
    print("[cyan]⚡ Setting up bdh-linux Terminal...[/cyan]")
    print("=" * 30)

    # Install ZSH
    print("[yellow]📦 Installing ZSH...[/yellow]")
    run("sudo pacman -S --noconfirm zsh git curl")

    # Oh My Zsh
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh")):
        print("[yellow]⚡ Installing Oh My Zsh...[/yellow]")
        run("git clone --depth=1 https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh")
    else:
        print("[yellow]⚡ Oh My Zsh already exists, skipping...[/yellow]")

    # Powerlevel10
    # Powerlevel10k
       
    # Powerlevel10k
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh/custom/themes/powerlevel10k")):
         run("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k")
    else:
         print("[yellow]⚡ Powerlevel10k already exists, skipping...[/yellow]")

# zsh-autosuggestions
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")):
         run("git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")
    else:
         print("[yellow]⚡ zsh-autosuggestions already exists, skipping...[/yellow]")

# zsh-syntax-highlighting
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")):
         run("git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")
    else:
         print("[yellow]⚡ zsh-syntax-highlighting already exists, skipping...[/yellow]")
     

    # Plugins
    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")):
        run("git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions.git ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions")

    if not os.path.isdir(os.path.expanduser("~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")):
        run("git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting")

    # BDH Configs — curl வழியா
    print("[yellow]🔧 Applying BDH configs...[/yellow]")
    run(f"curl -fsSL {BASE_URL}/configs/.zshrc -o ~/.zshrc")
    run(f"curl -fsSL {BASE_URL}/configs/aliases.sh -o ~/.aliases.sh")

    # Shell மாத்த
    run("sudo usermod -s /bin/zsh $USER")

    print("")
    print("[green]✅ Terminal setup done![/green]")
    print("[green]💡 Run 'p10k configure' to customize prompt![/green]")
    print("[green]⚡ Restart terminal to apply![/green]")
    print('reset') 

@app.command()
def packages():
    """Install all BDH packages"""
    print("[cyan]⚡ Setting up BDH Packages...[/cyan]")
    print("=" * 30)
    run(f"curl -fsSL {BASE_URL}/scripts/install-packages.sh -o /tmp/install-packages.sh")
    run("bash /tmp/install-packages.sh")
    print("")
    print("[green]✅ Packages setup done![/green]")

@app.command()
def git():
    """Setup Git global config"""
    print("[cyan]⚡ Setting up Git...[/cyan]")
    print("=" * 30)
    name = typer.prompt("Your name")
    Token = typer.prompt("Your email")
    run(f'git config --global user.name "{name}"')
    run(f'git config --global user.email "{Token}"')
    run("git config --global init.defaultBranch main")
    print("")
    print("[green]✅ Git setup done![/green]")

@app.command()
def docker():
    """Install and setup Docker"""
    print("[cyan]⚡ Setting up Docker...[/cyan]")
    print("=" * 30)
    run("sudo pacman -S --noconfirm docker docker-compose")
    run("sudo systemctl enable docker")
    run("sudo systemctl start docker")
    run("sudo usermod -aG docker $USER")
    print("")
    print("[green]✅ Docker setup done![/green]")
@app.command()
def keyboard_backlight():
    your_labtop =str(input("dell,asus,acer,msi,lenovo,hp :-"))
    level = int(input("brightness leval(0-3):-"))
    if 0 <= level <=3 :
        run(f"echo {level} | sudo tee /sys/class/leds/{ your_labtop}::kbd_backlight/brightness")
    else:
        print ("invalid input ")





    
    






