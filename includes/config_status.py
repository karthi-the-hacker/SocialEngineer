#!/usr/bin/env python

"""
SocialEngineer - Social Engineering Toolkit
-------------------------------------------

Author      : Karthikeyan (https://karthithehacker.com)
GitHub      : https://github.com/karthi-the-hacker
Project     : SocialEngineer - An all-in-one CLI framework for social engineering

License     : Open-source — strictly for educational and ethical hacking purposes ONLY.

Note to Users:
--------------
🔐 This tool is intended solely for educational use, research, and authorized security testing.
🚫 Unauthorized use of this tool on networks you do not own or lack permission to test is illegal.
❗ If you use or modify this code, PLEASE GIVE PROPER CREDIT to the original author.

Warning to Code Thieves:
------------------------
❌ Removing this header or claiming this project as your own without credit is unethical and violates open-source principles.
🧠 Writing your own code earns respect. Copy-pasting without attribution does not.
✅ Be an ethical hacker. Respect developers' efforts and give credit where it’s due.
"""
import shutil
import subprocess
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def is_cloudflared_installed():
    return shutil.which("cloudflared") is not None


def check_cloudflared():
    print(Fore.CYAN + "[*] Checking cloudflared setup..." + Style.RESET_ALL)
    
    if not is_cloudflared_installed():
        print(Fore.RED + "❌ cloudflared CLI is not installed.")
        print(Fore.YELLOW + "➡️  Follow installation instructions here:")
        print(Fore.YELLOW + "   https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation")
        sys.exit(1)

    # cloudflared doesn't require a token for basic tunnels; ensure it runs
    try:
        result = subprocess.run(["cloudflared", "version"], capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError()
    except Exception:
        print(Fore.RED + "⚠️  cloudflared binary is present but could not be executed.")
        sys.exit(1)

    print(Fore.GREEN + "✅ cloudflared is installed and functional!")
