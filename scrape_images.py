import requests
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlparse


url = 'https://nsano.com/'

domain = urlparse(url=url).netloc
print('doamin', domain)

requests = requests.get(url)
print('reques', requests)

soup = BeautifulSoup(requests.text, "html.parser")
print('soup', soup)

raw_links = soup.find_all("img")
print('raw_links', raw_links)

links = []
for i in links:
    link = i['src']
    if link.startswith("http"):
        links.append(link)
    else: 
        new_link = "https://" + domain + link
        links.append(new_link)


