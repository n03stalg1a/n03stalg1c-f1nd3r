import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Back
import threading
import time
from queue import Queue
import logging
import os
import sys
import random
import time

# Initialize colorama for colorful CLI
init(autoreset=True)

# Constants for proxy types
PROXY_TYPES = ["HTTP", "HTTPS", "SOCKS4", "SOCKS5"]

# Configuration for proxy sources
PROXY_SOURCES = [
    'https://www.sslproxies.org/',  # SSL Proxies
    'https://free-proxy-list.net/',  # Free Proxy List
    'https://www.us-proxy.org/',  # US Proxy
    'https://www.proxy-list.download/HTTP',  # Proxy List Download (HTTP)
    'https://www.socks-proxy.net/',  # SOCKS Proxy
    'https://www.hide-my-ip.com/proxylist.shtml',  # Hide My IP Proxies
    'https://www.proxy-listen.de/Proxy/Proxyliste.html',  # Proxy Listen
    'https://www.proxynova.com/proxy-server-list/',  # Proxy Nova
    'https://www.freeproxylists.net/',  # Free Proxy Lists
    'https://www.nordvpn.com/free-proxy-list/',  # NordVPN Proxy List
    'https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt',  # GitHub Raw Proxy List
    'https://github.com/TheSpeedX/PROXY-List/blob/master/http.txt',  # SpeedX Proxy List (GitHub)
    'https://github.com/fate0/proxylist/blob/master/proxylist.txt',  # Fate0 Proxy List (GitHub)
    'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',  # OpenProxyList (GitHub)
    'https://raw.githubusercontent.com/saschazesiger/Free-Proxy-List/master/proxy_list.txt',  # Free Proxy List (GitHub)
    'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',  # Jetkai Proxy List (GitHub)
    'https://raw.githubusercontent.com/mertguvencli/proxy-list/master/proxy-list/data.txt',  # MertGuvenCLI Proxy List
    'https://raw.githubusercontent.com/jhao104/proxylist/master/proxy/https.txt',  # Jhao104 Proxy List
    'https://raw.githubusercontent.com/almog74/proxies/master/proxies.txt',  # Almog Proxy List
    'https://raw.githubusercontent.com/spmason/proxy-list/master/https.txt',  # SPmason Proxy List
    'https://raw.githubusercontent.com/ossobn/Proxy-List/master/proxy_list.txt',  # OssoProxy List
    'https://raw.githubusercontent.com/ThePythonista/ProxyList/master/proxylist.txt',  # Pythonista Proxy List
    'https://raw.githubusercontent.com/empire7/Proxy-Lists/master/proxy-list.txt',  # Empire7 Proxy List
    'https://raw.githubusercontent.com/darkterminal/proxy-list/master/proxies.txt',  # DarkTerminal Proxy List
    'https://raw.githubusercontent.com/proxylist/proxylist/master/proxylist.txt'  # ProxyList Repository
]

# Setup logging for better traceability
logging.basicConfig(filename='proxy_finder.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to display the title and beautify the command line
def display_welcome_message():
    title = '''
   n03stalg1c f1nd3r
   _   _            _             _     _       
  | \ | |          | |           | |   (_)      
  |  \| |_   _ ___| |_ __ _ _ __ | |__  _ _ __  
  | . ` | | | / __| __/ _` | '_ \| '_ \| | '_ \ 
  | |\  | |_| \__ \ || (_| | |_) | | | | | | | |
  |_| \_|\__,_|___/\__\__,_| .__/|_| |_|_|_| |_|
                             | |                  
                             |_|                  
    '''
    print(Fore.CYAN + title)
    print(Fore.GREEN + "Welcome to n03stalg1c f1nd3r!")
    print(Fore.YELLOW + "This tool will help you find proxies from public sources.")
    print(Fore.CYAN + "Please select the type of proxies you're interested in:")

def get_proxy_list(proxy_type):
    print(Fore.CYAN + f"\nSearching for {proxy_type} proxies...")

    proxies = []
    queue = Queue()

    # Multi-threading for fetching proxies
    def fetch_from_site(site):
        try:
            response = requests.get(site, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            if 'github' in site:
                proxy_list = response.text.splitlines()
                for proxy in proxy_list:
                    queue.put(proxy.strip())
            else:
                # Handle regular sites with tables
                rows = soup.find('table').find_all('tr')[1:]
                for row in rows:
                    cols = row.find_all('td')
                    ip = cols[0].text.strip()
                    port = cols[1].text.strip()
                    https = cols[6].text.strip()

                    if (proxy_type == "HTTP" and https == 'no') or (proxy_type == "HTTPS" and https == 'yes'):
                        queue.put(f"{ip}:{port}")
        except Exception as e:
            logging.error(f"Error fetching proxies from {site}: {str(e)}")

    threads = []

    # Start fetching proxies from multiple sources simultaneously
    for site in PROXY_SOURCES:
        thread = threading.Thread(target=fetch_from_site, args=(site,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Collect all proxies
    while not queue.empty():
        proxies.append(queue.get())

    return proxies

def validate_proxy(proxy):
    """Validate a proxy by trying to fetch a URL."""
    try:
        test_url = "https://httpbin.org/ip"  # A simple IP check service
        proxies = {"http": f"http://{proxy}", "https": f"https://{proxy}"}
        response = requests.get(test_url, proxies=proxies, timeout=5)
        
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException:
        return False

def export_proxies_to_txt(proxies):
    print(Fore.YELLOW + "Exporting proxies to 'proxies.txt'...")

    with open('proxies.txt', 'w') as file:
        for proxy in proxies:
            file.write(proxy + "\n")

    print(Fore.GREEN + "Proxies exported successfully to proxies.txt!")

def display_progress_bar(current, total, prefix='', length=50):
    percent = (current / total) * 100
    filled_length = int(length * current // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent:.1f}% Complete', end='')

def main():
    display_welcome_message()

    # User input for proxy type
    while True:
        print(Fore.CYAN + "\nChoose proxy type:")
        for i, proxy_type in enumerate(PROXY_TYPES, 1):
            print(Fore.GREEN + f"{i}. {proxy_type}")
        choice = input("Enter the number corresponding to your choice: ")

        if choice in ['1', '2', '3', '4']:
            proxy_type = PROXY_TYPES[int(choice) - 1]
            break
        else:
            print(Fore.RED + "Invalid input. Please choose 1 for HTTP, 2 for HTTPS, 3 for SOCKS4, or 4 for SOCKS5.")

    # Fetch proxies
    proxies = get_proxy_list(proxy_type)

    if proxies:
        print(Fore.GREEN + f"\nFound {len(proxies)} {proxy_type} proxies.")
        valid_proxies = []
        
        # Validate proxies with progress bar
        print(Fore.YELLOW + "Validating proxies...")
        for i, proxy in enumerate(proxies, 1):
            display_progress_bar(i, len(proxies), prefix="Validating")
            if validate_proxy(proxy):
                valid_proxies.append(proxy)
                print(Fore.GREEN + f"{proxy} is working.")
            else:
                print(Fore.RED + f"{proxy} failed validation.")
        
        print(Fore.GREEN + f"\n{len(valid_proxies)} valid {proxy_type} proxies found.")
        
        # Ask user if they want to export the results
        export_choice = input(Fore.CYAN + "\nDo you want to export the valid proxies to a TXT file? (y/n): ").lower()
        if export_choice == 'y':
            export_proxies_to_txt(valid_proxies)
        else:
            print(Fore.RED + "Proxies not exported.")
    else:
        print(Fore.RED + f"No {proxy_type} proxies found.")

if __name__ == "__main__":
    main()
