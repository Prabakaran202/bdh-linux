#!/bin/bash

: <<'COMMENT'
//echo "⚡ Welcome to bdh-linux Setup!"
echo "================================"

BASE_URL="https://raw.githubusercontent.com/BackendDeveloperHub/bdh-linux/main"

# Step 1 — ZSH
echo "🔧 Setting up ZSH..."
sudo pacman -S --noconfirm zsh git curl
sudo usermod -s /bin/zsh $USER
# Step 2 — Ranger + Nano
echo "🗂️  Setting up Ranger with Nano..."
bash scripts/setup_ranger.sh

# Step 3 — Oh My Zsh
if [ ! -d "$HOME/.oh-my-zsh" ]; then
  echo "🔧 Installing Oh My Zsh..."
  git clone --depth=1 https://github.com/ohmyzsh/ohmyzsh.git ~/.oh-my-zsh
else
  echo "⚡ Oh My Zsh already exists, skipping..."
fi

# Step 4 — Powerlevel10k
if [ ! -d "$HOME/.oh-my-zsh/custom/themes/powerlevel10k" ]; then
  echo "🔧 Installing Powerlevel10k..."
  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
    ~/.oh-my-zsh/custom/themes/powerlevel10k
else
  echo "⚡ Powerlevel10k already exists, skipping..."
fi

# Step 5 — Plugins
if [ ! -d "$HOME/.oh-my-zsh/custom/plugins/zsh-autosuggestions" ]; then
  git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions.git \
    ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
fi

if [ ! -d "$HOME/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting" ]; then
  git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting.git \
    ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
fi

# Step 6 — BDH Configs
echo "🔧 Applying BDH configs..."
curl -fsSL "$BASE_URL/configs/.zshrc" -o ~/.zshrc
curl -fsSL "$BASE_URL/configs/aliases.sh" -o ~/.aliases.sh

# Step 7 — Packages
echo "🔧 Installing packages..."
curl -fsSL "$BASE_URL/scripts/install-packages.sh" -o /tmp/install-packages.sh
bash /tmp/install-packages.sh
# scripts/setup.sh - la ithai add pannunga
echo "Checking Internet Connection..."
if ! ping -c 1 google.com &> /dev/null; then
    echo "Internet illai! Network Link process-a start pandraen..."
    # Inga namma munnadi discuss panna nmcli logic-a call pannanum
fi

echo ""
echo "✅ bdh-linux Setup Complete!"
echo "================================"
echo "⚡ Restart terminal to apply changes!"
echo "💡 Run 'p10k configure' to customize your prompt!"
//
COMMENT
#!/bin/bash

echo "⚡ Welcome to bdh-linux Setup!"
echo "================================"

BASE_URL="https://raw.githubusercontent.com/BackendDeveloperHub/bdh-linux/main"

# --- STEP 0: Internet Check & Network Link ---
echo "🔍 Checking Internet Connection..."
if ! ping -c 1 google.com &> /dev/null; then
    echo "⚠️ Internet illai! Network Link process-a start pandraen..."
    
    # NetworkManager active-ah irukkannu check pannurom
    sudo systemctl enable --now NetworkManager &> /dev/null

    echo "🔭 Scanning for Wi-Fi networks..."
    nmcli device wifi rescan
    nmcli -f SSID,BARS,SECURITY device wifi list
    
    echo "--------------------------------"
    read -p "Select panna Wi-Fi Name (SSID): " ssid
    read -s -p "Wi-Fi Password: " password
    echo ""
    
    echo "⚡ Connecting to $ssid..."
    nmcli device wifi connect "$ssid" password "$password"
    
    # Thirumba check pannurom
    if ! ping -c 1 google.com &> /dev/null; then
        echo "❌ Connection fail aayiduchi! Internet illama setup thodara mudiyathu."
        exit 1
    fi
    echo "✅ Internet Connected! Setup thodaruthu..."
fi
# ---------------------------------------------

# Step 1 — ZSH
echo "🔧 Setting up ZSH..."
sudo pacman -S --noconfirm zsh git curl
# Step 2 — Ranger + Nano
echo "🗂️  Setting up Ranger..."
bash scripts/setup_ranger.sh
# ... (matha steps ellam appadiyae thodarum)
