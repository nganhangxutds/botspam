import requests
from concurrent.futures import ThreadPoolExecutor
import os
import sys
import time
from time import sleep
import pystyle
import random
import time
def slow_type(text, delay=0.00):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
def banner():
    slow_type("""


║➢ Admin   : Htrlee                                      
║➢ The Center Of All Power                
║➣ Thích Mà Không Nói Là Ngu - Thích Mà Nói Là Vừa Ngu Vừa Ảo Tưởng
                 

""", delay=0.00)
def clear():
    os.system("cls" if os.name == "nt" else "clear")
def thanh():
    print("\033[1;37m ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣ ➣")
# Bắt đầu chay tool
sleep(0)
clear()
banner()
thanh()
slow_type(" ")
sleep(0)
proxy_list = input("\033[1;32m File Proxy Cần Lọc: \033[1;33m")
with open(proxy_list, 'r') as file:
    proxy_list = file.read().split("\n")
    proxy_count = len(proxy_list)
luu = input("\033[1;31m File Proxy Live: \033[1;37m")
slow_type(f" \033[1;31mTất Cả Gồm: \033[1;37m{proxy_count} \033[1;31mProxy Trong File")
sleep(0)
slow_type(" \033[1;31mChờ Chút \033[1;37mTool \033[1;31mBắt Đầu \033[1;37mLọc \033[1;31mProxy")
sleep(0)
print(" \033[1;37mBắt Đầu \033[1;31mChạy \033[1;37mTool \033[1;31mLọc\033[1;37m. \033[1;31mVui Lòng \033[1;37mKhông \033[1;31mThoát \033[1;37mTermux")
print("\033[1;37m ———————————————————————————————————————————————")
sleep(3)
list = []
for p in proxy_list:
    prx = p.strip("\n")
    list.append(prx)


def check_proxy(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}'
    }
    
    try:
        response = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
        if response.status_code == 200 or response.status_code == 202 or response.status_code == 504 or response.status_code == 503 or response.status_code == 502 or response.status_code == 500:
            detect_location(proxy)
            open(luu,'a').write(proxy+'\n')
            return True
    except requests.exceptions.RequestException:
        pass

    print(f" \033[1;37m[\033[1;31m★\033[1;37m] \033[1;37m{proxy} \033[1;31m× \033[1;37mUnknown/Unknown \033[1;31m× \033[1;31mDie")
    return False


def detect_location(proxy):
    ip_address = proxy.split(':')[0]
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["status"] == "success":
            print(f" \033[1;37m[\033[1;31m★\033[1;37m] \033[1;37m{proxy} \033[1;31m√ \033[1;37m{data['country']}/{data['city']} \033[1;31m√ \033[1;32mLive")
            open(luu,'a').write(proxy+'\n')
        else:
            print(" \033[1;37m[\033[1;31m+\033[1;37m] \033[1;31mFailed to detect location for proxy.")


def process_proxy(proxy):
    if check_proxy(proxy):
        pass


num_workers = 200

with ThreadPoolExecutor(max_workers=num_workers) as executor:
    executor.map(process_proxy, proxy_list)

print(
    f" \033[1;31mScanning proxies successfully. Currently on the proxy list \033[1;37m{luu} \033[1;31mis having \033[1;37m%s \033[1;31mproxies-live"
    % (len(open(f"{luu}").readlines()))
)
print("\033[1;31m Thanks for using my tool<3")
logout = input(" Press enter to exit!")
exit()