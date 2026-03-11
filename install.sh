#!/bin/bash
set -e

# --------------------------
# Check for sudo/root
# --------------------------
if [ "$EUID" -ne 0 ]; then
    echo "[!] This script must be run as root or with sudo."
    echo "    Try: sudo $0"
    exit 1
fi

# --------------------------
# Show banner
# --------------------------
python3 - <<'END_PYTHON'
from includes import banner
from includes import utils
utils.check_sudo()  # optional double-check in Python
banner.show_banner()
END_PYTHON

# --------------------------
# Begin installation
# --------------------------
echo "[*] Updating system packages..."
apt update -y
apt upgrade -y
apt install tor -y

echo "[*] Installing Python3, pip, and Tor..."
if ! apt install -y python3 python3-pip tor; then
    echo "[!] Failed to install Python3/pip/Tor."
    echo "    Please check your package manager or network and install manually:"
    echo "    apt install python3 python3-pip tor"
    exit 1
fi

echo "[*] Installing Python requirements..."
if [ -f requirements.txt ]; then
    if ! pip3 install -r requirements.txt; then
        echo "[!] Normal pip install failed. Retrying with --break-system-packages..."
        if ! pip3 install --break-system-packages -r requirements.txt; then
            echo "[!] Failed to install Python requirements. Please install manually:"
            echo "    pip3 install -r requirements.txt"
            exit 1
        fi
    fi
else
    echo "[!] requirements.txt not found, skipping Python deps."
fi

# reminder for cloudflared installation
echo "[*] Note: this installer does not configure cloudflared.
      Please download the cloudflared CLI from Cloudflare or install
      via your package manager. See:
      https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation"

# --------------------------
# Configure Tor
# --------------------------
TORRC_FILE="/etc/tor/torrc"

echo "[*] Configuring Tor control port (9051) with cookie authentication..."
cp "$TORRC_FILE" "${TORRC_FILE}.bak.$(date +%s)"
sed -i '/^ControlPort/d' "$TORRC_FILE"
sed -i '/^CookieAuthentication/d' "$TORRC_FILE"
echo "ControlPort 9051" | tee -a "$TORRC_FILE" > /dev/null
echo "CookieAuthentication 1" | tee -a "$TORRC_FILE" > /dev/null

echo "[*] Restarting Tor to apply configuration..."
if ! systemctl restart tor; then
    echo "[!] Failed to start Tor automatically."
    echo "    Please start Tor manually and check logs:"
    echo "    systemctl status tor"
    exit 1
fi

echo "[*] Installation and configuration complete."
