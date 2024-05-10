import asyncio
import httpx

async def fetch_data(url, session):
    try:
        response = await session.get(url)
        return response.text
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return None

async def main():
    urls = [
        'https://ciapak-proxy.cf/api/paid/?key=980321830129381029&type=http',
        'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all&ssl=all&anonymity=all',
        'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
        'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
        'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
        'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
        'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt'
		   "https://api.proxyscrape.com/?request=displayproxies&proxytype=http",
                   "https://api.openproxylist.xyz/http.txt",
                   "http://alexa.lr2b.com/proxylist.txt",
                   "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                   "http://worm.rip/http.txt",
                   "https://proxy-spider.com/api/proxies.example.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://proxyspace.pro/http.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
                   "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt",
                   "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt",
                   "https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/https/https.txt",
                   "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                   "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
                   "https://openproxylist.xyz/http.txt",
                   "https://dodanhtai.site/proxy/http.txt",
                   "http://worm.rip/http.txt",
                   "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/http.txt",
                   "http://rootjazz.com/proxies/proxies.txt",
                   "https://api.proxyscrape.com/?request=displayproxies&proxytype=https",
                   "https://www.proxy-list.download/api/v1/get?type=http",
                   "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
                   "https://api.openproxylist.xyz/http.tx",
                   "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
                   "http://alexa.lr2b.com/proxylist.txt",
                   "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
                   "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
                   "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
                   "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
                   "https://proxy-spider.com/api/proxies.example.txt",
                   "https://multiproxy.org/txt_all/proxy.txt",
                   "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                   "https://proxyspace.pro/http.txt",
                   "https://proxyspace.pro/https.txt",
                   "https://proxyspace.pro/https.txt",
                   "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
                   "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
                   "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
                   "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
                   "https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
                   "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
                   "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
                   "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
                   "https://rootjazz.com/proxies/proxies.txt",
                   "https://www.proxy-list.download/api/v1/get?type=https",
                   "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt",
                   "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt",
                   "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt",
                   "https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt",
                   "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
                   "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
                   "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies_anonymous/http.txt",
                   "https://raw.githubusercontent.com/rdavydov/proxy-list/main/proxies/http.txt",
                   "https://sunny9577.github.io/proxy-scraper/proxies.txt",
                   "https://api.getproxylist.com/proxy?protocol[]=http&anonymity[]=high&allowsHttps=true&allowsPost=true&maxConnectTime=1&maxSecondsToFirstByte=1",
    ]

    async with httpx.AsyncClient() as session:
        tasks = [fetch_data(url, session) for url in urls]
        results = await asyncio.gather(*tasks)

        # Save the results to a single file (zmap.txt)
        with open("proxyget.txt", 'w') as file:
            for result in results:
                if result is not None:
                    file.write(result)
                    file.write("\n\n")
                    print("Data appended to proxyget.txt")

    # Remove empty lines from zmap.txt
    clean_up_http_file()

def clean_up_http_file():
    with open("proxyget.txt", 'r') as file:
        lines = file.readlines()

    with open("proxyget.txt", 'w') as file:
        for line in lines:
            if line.strip():
                file.write(line)

if __name__ == "__main__":
    asyncio.run(main())
