
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
import re
import subprocess

# store the cloudflared process so it can be stopped later
_tunnel_proc = None

def re_url():
    """Start a cloudflared tunnel and return the public URL.

    The tunnel process is left running in the background; callers
    should call :func:`stop_tunnel` when finished to clean up.
    """
    global _tunnel_proc

    # launch cloudflared and capture stdout so we can parse the URL
    _tunnel_proc = subprocess.Popen(
        ["cloudflared", "tunnel", "--url", "http://localhost:80"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )

    url = None
    # read lines until a trycloudflare URL appears
    for line in _tunnel_proc.stdout:
        # look for a trycloudflare address (http or https)
        match = re.search(r'https?://[A-Za-z0-9\-]+\.trycloudflare\.com', line)
        if match:
            url = match.group(0)
            break

    if not url:
        raise RuntimeError("Unable to obtain Cloudflared public URL")

    return url

def stop_tunnel():
    """Terminate the running cloudflared tunnel process, if any."""
    global _tunnel_proc
    if _tunnel_proc:
        try:
            _tunnel_proc.terminate()
        except Exception:
            pass
        _tunnel_proc = None