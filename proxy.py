import httpx

with open("proxy.txt", 'w') as file:
	file.write(httpx.get("https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&proxy_format=ipport&format=text").text)

