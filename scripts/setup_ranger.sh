#!/bin/bash

# BDH Linux — Ranger + Nano Setup

echo "🗂️  Setting up Ranger with Nano editor..."

# Install ranger and nano
sudo pacman -S ranger nano --noconfirm

# Create ranger config directory
mkdir -p ~/.config/ranger

# Copy default config if not exists
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