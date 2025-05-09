import requests
import json 
from art import *
import time


GREEN = "\033[92m"
YELLOW = "\033[93m" 

CYAN = "\033[96m"   
RESET = "\033[0m"
BLUE = "\033[94m"
RED = "\033[91m"
PURPLE = "\033[95m"  

art_text = text2art("GhostFinder", font="big")


print(GREEN + art_text+  RESET )
print(GREEN+'='*80+RESET)
print(CYAN+"[ 🔍 ] GhostFinder tool for searching usernames across websites"+RESET)
print(GREEN+"[ ✅ ] You can search for one or multiple names at the same time"+RESET)
print(CYAN+"[ 🎯 ] Enter the username. You can enter multiple names separated by spaces"+RESET)
print(GREEN+"=" * 80 + RESET)

def load_sites(file_path='data.schema.json'):
    try:
        with open(file_path,'r',encoding='utf-8') as file:
            return json.load(file)
        
    except FileNotFoundError :
        print("Error: File sites.json not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return {}


def scan_name(usernames):
    sites = load_sites()
    if not sites:
        print('NO Sites loaded .Exiting...')

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    total_sites = len(sites)
    estimated_timer = 3.5
    all_timer = total_sites * estimated_timer
    print(f"\n{CYAN}[*] Estimated scan time: {all_timer:.2f} seconds.{RESET}")
    

    print("\n")



    
    for user in usernames:
        print(f"\n{CYAN}[{GREEN}={CYAN}] Scanning for username{RESET}: {user} \n")
        for site , data in sites.items():
            try:
                if 'url'in data:
                    full_url = data['url'].format(user)
                
                    response = requests.get(full_url,headers=headers)
                    if response.status_code == 200 :
                        if "User not found" in response.text:
                            print(f"[NOT FOUND] {url}")
                        else:
                            print(f"[{GREEN}+{RESET}] {GREEN}{site}{RESET}: {full_url}")
                   
            except Exception :
                print(f"{GREEN}[{RED}-{GREEN}]{RESET} {RED}Error:{RESET} SSL Certificate Error")
    



if __name__ == "__main__":
    usernames = input(f"{GREEN}${RESET}[Enter{GREEN}_{RESET}username]{GREEN}:{RESET}").split()
    start_time = time.time()
    scan_name(usernames)
    
