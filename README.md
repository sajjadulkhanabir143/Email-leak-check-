```text
==================================================
█████  ███     ██    ██  ███  ████  ██ ██ ██   
██    ██ ██    ██    ██ ██ ██ ██ ██ ██ ██ ██   
█████ █████    ██    ██ █████ ██ ██ ██ ██ ██   
   ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██   
█████ ██ ██  ███   ███  ██ ██ ████   ███  █████

██ ██ ██ ██  ███  ██  █    ███  ████  ████ ████ 
██ ██ ██ ██ ██ ██ ███ █   ██ ██ ██ ██  ██  ██ ██
████  █████ █████ ██ ██   █████ ████   ██  ████ 
██ ██ ██ ██ ██ ██ █ ███   ██ ██ ██ ██  ██  ██ ██
██ ██ ██ ██ ██ ██ █  ██   ██ ██ ████  ████ ██ ██
==================================================
      [*] Email OSINT & Lookup Tool v1.0
      [*] Developed by: Sajjadul Khan Abir
==================================================
```

# Email Leak Check & OSINT Tool

**Author:** **Sajjadul Khan Abir**

A fast, lightweight, and API-key-free **Email Leak Check & OSINT Reconnaissance Tool** built with Python, specifically optimized for **Termux (Android)** and **Linux** terminals.

## Features

- **Syntax Validation:** Checks whether the target email follows a valid format.
- **Disposable Email Detection:** Identifies temporary/throwaway email domains (e.g., Mailinator, 10MinuteMail, GuerrillaMail, YOPmail, Temp-Mail).
- **DNS & MX Record Check:** Queries live Mail Exchange (MX) servers to verify if the domain can actively receive emails.
- **Gravatar Profile Lookup:** Searches for linked public Gravatar profiles (display name and profile URL) using SHA-256 email hashing.
- **Data Breach Check:** Checks if the email address has been exposed in known public data breaches via the XposedOrNot API.
- **Interactive CLI Loop:** Allows continuous lookups in a single session until you type `exit` or `quit`.

## Requirements

- Python 3.7+
- `requests`
- `dnspython`

## Installation (Termux)

1. Update Termux packages and install Python & Git:
   ```bash
   pkg update && pkg upgrade -y
   pkg install python git -y
   ```

2. Clone the repository and enter the directory:
   ```bash
   git clone [https://github.com/sajjadulkhanabir143/Email-leak-check-.git](https://github.com/sajjadulkhanabir143/Email-leak-check-.git)
   cd Email-leak-check-
   ```

3. Install required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the tool in Termux:

```bash
python email_lookup.py
```

Enter the email address you want to inspect. To close the program, type `exit`, `quit`, or `q`.

### Example Output

```text
==================================================
[*] Target Email: example@gmail.com
==================================================
[+] Syntax: Valid format
[+] Domain: gmail.com
[+] Provider Type: Standard domain
[+] Mail Servers (MX): Active (5 found)
    - Priority 5: gmail-smtp-in.l.google.com
    - Priority 10: alt1.gmail-smtp-in.l.google.com
[-] Gravatar Profile: Not found
[+] Data Breaches: No public breaches found
==================================================
```

## Disclaimer

This tool is created strictly for **educational purposes, authorized security testing, and personal privacy auditing**. The author (**Sajjadul Khan Abir**) is not responsible for any misuse or unauthorized reconnaissance conducted with this script.

