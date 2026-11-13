import hashlib
import os
import re
import dns.resolver
import requests

# Terminal Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD_CYAN = "\033[1;96m"
BOLD_GREEN = "\033[1;92m"
BOLD_YELLOW = "\033[1;93m"
RESET = "\033[0m"

DISPOSABLE_DOMAINS = {
    "mailinator.com",
    "10minutemail.com",
    "tempmail.com",
    "guerrillamail.com",
    "yopmail.com",
    "throwawaymail.com",
    "trashmail.com",
    "temp-mail.org",
    "sharklasers.com",
}


def print_banner():
  os.system("clear")
  banner = f"""{BOLD_CYAN}
==================================================
█████  ███     ██    ██  ███  ████  ██ ██ ██   
██    ██ ██    ██    ██ ██ ██ ██ ██ ██ ██ ██   
█████ █████    ██    ██ █████ ██ ██ ██ ██ ██   
   ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██   
█████ ██ ██  ███   ███  ██ ██ ████   ███  █████

{BOLD_GREEN}██ ██ ██ ██  ███  ██  █    ███  ████  ████ ████ 
██ ██ ██ ██ ██ ██ ███ █   ██ ██ ██ ██  ██  ██ ██
████  █████ █████ ██ ██   █████ ████   ██  ████ 
██ ██ ██ ██ ██ ██ █ ███   ██ ██ ██ ██  ██  ██ ██
██ ██ ██ ██ ██ ██ █  ██   ██ ██ ████  ████ ██ ██
{BOLD_CYAN}==================================================
{BOLD_YELLOW}      [*] Email OSINT & Lookup Tool v1.0
      [*] Developed by: Sajjadul Khan Abir{BOLD_CYAN}
=================================================={RESET}
"""
  print(banner)


def validate_syntax(email):
  pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  return re.match(pattern, email) is not None


def check_mx_records(domain):
  try:
    records = dns.resolver.resolve(domain, "MX")
    return sorted([(r.preference, str(r.exchange).rstrip(".")) for r in records])
  except Exception:
    return []


def check_gravatar(email):
  clean_email = email.strip().lower().encode("utf-8")
  sha256_hash = hashlib.sha256(clean_email).hexdigest()
  url = f"https://gravatar.com/{sha256_hash}.json"
  try:
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=8)
    if res.status_code == 200:
      data = res.json()
      entry = data.get("entry", [{}])[0]
      return {
          "found": True,
          "display_name": entry.get("displayName", "N/A"),
          "profile_url": entry.get(
              "profileUrl", f"https://gravatar.com/{sha256_hash}"
          ),
      }
  except Exception:
    pass
  return {"found": False}


def check_breaches(email):
  url = f"https://api.xposedornot.com/v1/check-email/{email}"
  try:
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    if res.status_code == 200:
      data = res.json()
      breaches = data.get("breaches", [])
      if breaches and isinstance(breaches[0], list):
        return breaches[0]
      return breaches
  except Exception:
    pass
  return []


def lookup_email(email):
  print(f"\n{CYAN}=================================================={RESET}")
  print(f"{CYAN}[*] Target Email:{RESET} {email}")
  print(f"{CYAN}=================================================={RESET}")

  # 1. Syntax Check
  if not validate_syntax(email):
    print(f"{RED}[!] Invalid Email Format!{RESET}")
    return
  print(f"{GREEN}[+] Syntax:{RESET} Valid format")

  domain = email.split("@")[1].lower()
  print(f"{GREEN}[+] Domain:{RESET} {domain}")

  # 2. Disposable Check
  if domain in DISPOSABLE_DOMAINS:
    print(f"{YELLOW}[!] Provider Type:{RESET} Temporary / Disposable email")
  else:
    print(f"{GREEN}[+] Provider Type:{RESET} Standard domain")

  # 3. MX Record Check
  mx_records = check_mx_records(domain)
  if mx_records:
    print(
        f"{GREEN}[+] Mail Servers (MX):{RESET} Active ({len(mx_records)}"
        " found)"
    )
    for pref, host in mx_records:
      print(f"    - Priority {pref}: {host}")
  else:
    print(f"{RED}[-] Mail Servers (MX):{RESET} None found")

  # 4. Gravatar Check
  grav = check_gravatar(email)
  if grav["found"]:
    print(f"{GREEN}[+] Gravatar Profile:{RESET} Found!")
    print(f"    - Name: {grav['display_name']}")
    print(f"    - URL : {grav['profile_url']}")
  else:
    print(f"{YELLOW}[-] Gravatar Profile:{RESET} Not found")

  # 5. Breach Check
  breaches = check_breaches(email)
  if breaches:
    print(
        f"{RED}[!] Data Breaches:{RESET} Exposed in {len(breaches)} breach(es):"
    )
    print(f"    - {', '.join(breaches)}")
  else:
    print(f"{GREEN}[+] Data Breaches:{RESET} No public breaches found")

  print(f"{CYAN}=================================================={RESET}\n")


if __name__ == "__main__":
  print_banner()
  while True:
    target = input("Enter email to lookup (or 'exit' to quit): ").strip()
    if target.lower() in ("exit", "quit", "q"):
      print(f"{YELLOW}[*] Exiting tool. Goodbye!{RESET}")
      break
    if target:
      lookup_email(target)

