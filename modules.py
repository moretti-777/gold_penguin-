#!/usr/bin/env python3
import os
import json
import urllib.request
import socket
import ssl
import sys

GOLD = "\033[38;5;214m"
YELLOW = "\033[1;33m"
WHITE = "\033[1;37m"
RED = "\033[31m"
GREEN = "\033[32m"
GREY = "\033[90m"
RESET = "\033[0m"

ssl_context = ssl._create_unverified_context()

def format_ip_data(data):
    if data.get("status") == "fail":
        print(f"{RED}[-] API Server Error: {data.get('message', 'Invalid IP target')}{RESET}")
        return
    print(f" {GOLD}╔═════════════════════════════════════════════════════╗{RESET}")
    print(f" {GOLD}║                INVESTIGATION RESULTS                ║{RESET}")
    print(f" {GOLD}╚═════════════════════════════════════════════════════╝{RESET}\n")
    print(f" {GOLD}•{WHITE} IP Address:{RESET}       {data.get('query')}")
    print(f" {GOLD}•{WHITE} Connection Type:{RESET}  {data.get('type', 'N/A')}")
    print(f" {GOLD}•{WHITE} Country/State:{RESET}    {data.get('country')} ({data.get('countryCode')})")
    print(f" {GOLD}•{WHITE} Region/State:{RESET}     {data.get('regionName')} ({data.get('region')})")
    print(f" {GOLD}•{WHITE} City/Location:{RESET}    {data.get('city')}")
    print(f" {GOLD}•{WHITE} ZIP / Postal:{RESET}     {data.get('zip', 'N/A')}")
    print(f" {GOLD}•{WHITE} Timezone:{RESET}         {data.get('timezone')}")
    print(f" {GOLD}•{WHITE} ISP Provider:{RESET}     {data.get('isp')}")
    print(f" {GOLD}•{WHITE} Organization:{RESET}     {data.get('org', 'N/A')}")
    print(f" {GOLD}•{WHITE} AS / Autonomous:{RESET}  {data.get('as')}")
    print(f" {GOLD}•{WHITE} Latitude:{RESET}         {data.get('lat')}")
    print(f" {GOLD}•{WHITE} Longitude:{RESET}        {data.get('lon')}")

def my_ip():
    print(f"{GOLD}[*]{WHITE} Querying remote databases to detect your public IP...{RESET}\n")
    try:
        url = "http://ip-api.com"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ssl_context, timeout=10) as response:
            format_ip_data(json.loads(response.read().decode()))
    except Exception as e:
        print(f"{RED}[-] Connection error: Unable to retrieve your IP ({e}){RESET}")

def track_ip():
    target = input(f"{GOLD}[?]{WHITE} Enter target IP address to track: {RESET}").strip()
    if not target: return
    print(f"\n{GOLD}[*]{WHITE} Establishing secure lookup connection for {target}...{RESET}\n")
    try:
        url = f"http://ip-api.com{target}?fields=66846719"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ssl_context, timeout=10) as response:
            format_ip_data(json.loads(response.read().decode()))
    except Exception as e:
        print(f"{RED}[-] Error: Failed to query lookup database ({e}){RESET}")

def dns_recon():
    domain = input(f"{GOLD}[?]{WHITE} Enter target domain to analyze: {RESET}").strip()
    if not domain: return
    domain = domain.replace("https://", "").replace("http://", "").split('/')[0]
    print(f"\n{GOLD}[*]{WHITE} Initiating DNS forward resolution for host: {domain}...{RESET}\n")
    try:
        ip_address = socket.gethostbyname(domain)
        print(f" {GREEN}[✓]{WHITE} Domain successfully resolved!{RESET}\n")
        print(f" {GOLD}•{WHITE} Domain Name:{RESET}   {domain}")
        print(f" {GOLD}•{WHITE} Associated IP:{RESET} {ip_address}")
    except Exception as e:
        print(f"{RED}[-] Error: Remote host could not be resolved ({e}){RESET}")

def phone_osint():
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone
    except ImportError:
        print(f"{RED}[-] Error: Please run 'pip install phonenumbers' first.{RESET}")
        return
    phone_input = input(f"{GOLD}[?]{WHITE} Enter phone number (e.g., +393331234567): {RESET}").strip()
    if not phone_input: return
    try:
        parsed_number = phonenumbers.parse(phone_input, None)
        print(f"\n {GOLD}╔═════════════════════════════════════════════════════╗{RESET}")
        print(f" {GOLD}║               PHONE METADATA RESULTS                ║{RESET}")
        print(f" {GOLD}╚═════════════════════════════════════════════════════╝{RESET}\n")
        print(f" {GOLD}•{WHITE} Valid Structure:{RESET} {phonenumbers.is_valid_number(parsed_number)}")
        print(f" {GOLD}•{WHITE} Country Code:{RESET}    +{parsed_number.country_code}")
        print(f" {GOLD}•{WHITE} National Number:{RESET} {parsed_number.national_number}")
        print(f" {GOLD}•{WHITE} Assigned Region:{RESET} {geocoder.description_for_number(parsed_number, 'en')}")
        print(f" {GOLD}•{WHITE} Carrier/Brand:{RESET}   {carrier.name_for_number(parsed_number, 'en')}")
        print(f" {GOLD}•{WHITE} Timezone Group:{RESET} {', '.join(timezone.time_zones_for_number(parsed_number))}")
    except Exception as e:
        print(f"{RED}[-] Parsing failed: {e}{RESET}")

def osint_social():
    username = input(f"{GOLD}[?]{WHITE} Enter target username: {RESET}").strip()
    if not username: return
    print(f"\n{GOLD}[*]{WHITE} Scanning live platforms for: {username}...{RESET}\n")
    platforms = {
        "GitHub": f"https://github.com{username}",
        "Instagram": f"https://instagram.com{username}/",
        "TikTok": f"https://tiktok.com@{username}",
        "Reddit": f"https://reddit.com{username}"
    }
    for name, url in platforms.items():
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, context=ssl_context, timeout=5) as response:
                if response.status == 200:
                    print(f" [{GREEN}✓{RESET}] {name}: FOUND -> internal account matches format.")
        except Exception:
            print(f" [{RED}✕{RESET}] {name}: Not Found / Protected")

def port_scanner():
    target = input(f"{GOLD}[?]{WHITE} Enter target host or IP: {RESET}").strip()
    if not target: return
    print(f"\n{GOLD}[*]{WHITE} Scanning standard network ports on {target}...{RESET}\n")
    ports = [21, 22, 23, 25, 53, 80, 110, 443, 8080]
    try:
        target_ip = socket.gethostbyname(target)
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1.0)
            if s.connect_ex((target_ip, port)) == 0:
                print(f"  ↳ Port {GREEN}{port}{RESET}: OPEN")
            s.close()
    except Exception as e:
        print(f"{RED}[-] Scanner failed: {e}{RESET}")

def mx_analyzer():
    domain = input(f"{GOLD}[?]{WHITE} Enter email domain (e.g., domain.com): {RESET}").strip()
    if not domain: return
    domain = domain.split('@')[-1]
    print(f"\n{GOLD}[*]{WHITE} Querying local MX registers for {domain}...{RESET}\n")
    try:
        mx_records = os.popen(f"nslookup -type=mx {domain}").read()
        if "mail exchanger" in mx_records or "exchanger" in mx_records:
            print(f" {GREEN}[✓]{WHITE} Mail Server Infrastructure Found:{RESET}")
            for line in mx_records.split('\n'):
                if "exchanger" in line: print(f"  ↳ {line.strip()}")
        else:
            print(f"{YELLOW}[!] No public mail servers found for this host.{RESET}")
    except Exception as e:
        print(f"{RED}[-] Local subsystem failed: {e}{RESET}")
