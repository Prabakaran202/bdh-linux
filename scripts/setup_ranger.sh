#!/bin/bash

# BDH Linux — Ranger + Nano Setup

echo "🗂️  Setting up Ranger with Nano editor..."

# Install ranger and nano
if command -v pacman &> /dev/null; then
    sudo pacman -S ranger nano --noconfirm
elif command -v pkg &> /dev/null; then
    pkg install ranger nano -y
fi

# Create ranger config
mkdir -p ~/.config/ranger
if [ ! -f ~/.config/ranger/rc.conf ]; then
    ranger --copy-config=rc 2>/dev/null
fi

# Set nano as default editor
if grep -q "set editor" ~/.config/ranger/rc.conf; then
    sed -i 's/set editor.*/set editor nano/' ~/.config/ranger/rc.conf
else
    echo "set editor nano" >> ~/.config/ranger/rc.conf
fi

echo "✅ Ranger configured with Nano!"
echo "Run: ranger"