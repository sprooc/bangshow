#!/bin/bash

# Check if chafa is installed
if command -v chafa &> /dev/null; then
    echo "chafa is already installed."
else
    echo "chafa is not installed. Attempting to install..."

    # Detect the operating system
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux system
        if [ -f /etc/arch-release ]; then
            # Arch Linux
            echo "Detected Arch Linux. Installing chafa using pacman."
            sudo pacman -S chafa
        elif [ -f /etc/debian_version ]; then
            # Debian/Ubuntu system
            echo "Detected Debian/Ubuntu. Installing chafa using apt."
            sudo apt update
            sudo apt install chafa
        elif [ -f /etc/redhat-release ]; then
            # Red Hat/CentOS/Fedora system
            echo "Detected Red Hat/CentOS/Fedora. Installing chafa using dnf."
            sudo dnf install chafa
        else
            echo "Unsupported Linux distribution."
            exit 1
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        echo "Detected macOS. Installing chafa using Homebrew."
        brew install chafa
    else
        echo "Unsupported operating system: $OSTYPE"
        exit 1
    fi

    echo "chafa installation completed."
fi

# Create a virtual environment in ~/.bangshow
BANGSHOW_DIR="$HOME/.bangshow"

# Create the directory if it doesn't exist
mkdir -p "$BANGSHOW_DIR"

# Create a virtual environment
VENV_DIR="$BANGSHOW_DIR/venv"
python -m venv "$VENV_DIR"

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Install the bangshow package (you might want to replace this with the actual installation command)
pip install .

# Create a symlink to make bangshow accessible from anywhere
echo "Creating a symlink for bangshow in /usr/bin"
sudo rm -f "/usr/bin/bangshow"
sudo ln -s "$BANGSHOW_DIR/venv/bin/bangshow" "/usr/bin/bangshow"


echo "Installation complete! You can now run 'bangshow' from anywhere."
