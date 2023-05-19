import requests
import time 
import os 
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)
import pyfiglet



#FOR CLEAR SCREEN
try:
    os.system("cls")
except Exception as e:
    print("sorry")
os.system("clear")
while True:
    print(f"\n {Back.RED}[----------THIS TOOL MADE ONLY FOR EDUCATION PURPOSE----------]\n")
    banner = pyfiglet.figlet_format("DNS LOOKUP")
    print(banner)
    #HEADING LINES  
    print(f"{Back.RED}\t||----------DNS LOOKUP TOOLS----------||\n")
    print(f"\t\t{Fore.BLUE}DEVELOPED BY : YASH MANDLOI")

    #STARTING MIDDLE LINE 
    print(f"\n{Fore.GREEN}==================================================") 
    print("[ 01 ] DNS LOOKUP TOOL ")
    print("[ 02 ] ABOUT THIS TOOLS ")
    print("[ 03 ] EXIT ")
    print("[ 04 ] IMPORTANT NOTE ")
    print(f"{Fore.GREEN}==================================================")

    ch = input("ENTER YOUR CHOISE HERE : ")

    if ch == "1":

        #MAIN LOGIC START............... 
        # ..............YOU NEED YOUR HACKER TARGET API
        url = "https://api.hackertarget.com/dnslookup/?q="

        #YOUR TARGET 
        target = input(f"\n ENTER YOUR TARGET URL : {Fore.CYAN} ")

        mainurl = url+target

        req = requests.get(mainurl)

        print("\n TARGET DNS DETAILS \n")
        time.sleep(2)
        print(req.text)
        time.sleep(10)
        os.system("clear")
        #MAIN PATH END .......!!

    #ABOUT THIS TOOLS LINE 
    elif ch == "2":
        os.system("clear")
        
        print(f"\t\t{Back.RED} ABOUT TOOL \n")
        print("\t\t\t >> THIS TOOL FIND DOMAIN NAME SYSTEM ")
        print(f"\n{Back.BLUE} THIS TOOLS MADE ONLY FOR EDUCATION AND LEARNING PURPOSE \n")
        print(f"{Fore.BLUE}=================================================================")
        ban = pyfiglet.figlet_format("DEVELOPER YASH")
        print(ban)
        print(f"{Fore.BLUE}=================================================================")
        time.sleep(5)
        os.system('clear')
     
    #EXIT METHOD
    elif ch == "3":
        print(f"\n{Fore.CYAN} THANKS FOR USING ME ")
        time.sleep(2)
        os.system("clear")
        break

    elif ch == "4":
        os.system("clear")
        print(f"\t{Back.RED} NOTE")
        print(f"\n{Fore.GREEN} 1. THIS TOOL ONLY SUPPORT ON MAC OS OR LINUX BUT COMING SOON FOR WINDOWS")
        time.sleep(2)
        print(f"\n{Fore.GREEN} 2. BEFORE USING THIS TOOLS PLEASE CHECK YOUR INTERNET CONNECTION ")
        time.sleep(2)
        print(f"\n{Fore.GREEN} 3. THIS TOOLS ONLY MADE FOR EDUCATION PURPOSE ")
        time.sleep(8)
        os.system("clear")
        break
    
    
    else:
        os.system("clear")
        print(f"\n{Fore.RED} INVALID SYNTEX ")
        time.sleep(2)
        break
