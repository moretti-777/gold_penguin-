#!/usr/bin/env python3
import os
import sys
import time

try:
    import modules
except ImportError:
    print("\033[31m[-] Error: The 'modules.py' file was not found in the same directory.\033[0m")
    sys.exit(1)

WHITE = "\033[1;37m"
YELLOW = "\033[1;33m"
GREY = "\033[90m"
RESET = "\033[0m"

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def pause():
    print(f"\n{GREY}[*] Operation completed.{RESET}")
    input("\033[38;5;214mPress [Enter] to return to the main menu...{RESET}")

def banner():
    colors = ["\033[38;5;214m", "\033[38;5;208m", "\033[38;5;202m", "\033[38;5;196m", "\033[38;5;165m", "\033[38;5;129m", "\033[38;5;93m"]
    penguin = [
        f"{WHITE}       ▄███▄      ", f"{WHITE}      ██▀ ▀██     ", f"{WHITE}     ██ █ █ ██    ", f"{WHITE}     ▄█  {YELLOW}▼{WHITE}  █▄     ",
        f"{WHITE}    ███████████   ", f"{WHITE}    ███████████   ", f"{WHITE}     █████████    ", f"{WHITE}      ▀█████▀     ", f"       {YELLOW}▄█ █▄      "
    ]
    figlet = [
        "  ____       _     _   ____                               ",
        " / ___| ___ | | __| | |  _ \\  ___ _ __   __ _ _   _ _ _ __  ",
        "| |  _ / _ \\| |/ _` | | |_) |/ _ \\ '_ \\ / _` | | | | | '_ \\ ",
        "| |_| | (_) | | (_| | |  __/|  __/ | | | (_| | |_| | | | | |",
        " \\____|\\___/|_|\\__,_| |_|    \\___|_| |_|\\__, |\\__,_|_|_| |_|",
        "                                        |___/               ",
        "     ==============================================="
    ]
    print()
    for i in range(max(len(penguin), len(figlet))):
        p_part = penguin[i] if i < len(penguin) else "                  "
        f_part = figlet[i] if i < len(figlet) else ""
        print(f"{p_part}{colors[i % len(colors)]}{f_part}{RESET}")
    print(f"                                       {GREY}v1.0.0 - RECON FRAMEWORK{RESET}\n")

def main():
    while True:
        clear_screen()
        banner()
        print(f" {WHITE}1) IP Tracker (Target Lookup)")
        print(f" {WHITE}2) Check My Public IP")
        print(f" {WHITE}3) Domain / DNS Reconnaissance")
        print(f" {WHITE}4) Phone Number Parser")
        print(f" {WHITE}5) Live Social Username Scanner")
        print(f" {WHITE}6) Network Port Scanner")
        print(f" {WHITE}7) DNS MX Record Analyzer")
        print(f" {WHITE}0) Exit Framework\n")
        
        choice = input("\033[38;5;214mSelect an option > {RESET}").strip()
        
        if choice == "1":
            clear_screen(); modules.track_ip(); pause()
        elif choice == "2":
            clear_screen(); modules.my_ip(); pause()
        elif choice == "3":
            clear_screen(); modules.dns_recon(); pause()
        elif choice == "4":
            clear_screen(); modules.phone_osint(); pause()
        elif choice == "5":
            clear_screen(); modules.osint_social(); pause()
        elif choice == "6":
            clear_screen(); modules.port_scanner(); pause()
        elif choice == "7":
            clear_screen(); modules.mx_analyzer(); pause()
        elif choice == "0":
            clear_screen()
            print(f"{YELLOW}Thank you for using Gold Penguin! Goodbye.{RESET}")
            sys.exit(0)
        else:
            print(f"\n\033[31m[!] Invalid choice. Please try again.\033[0m")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
