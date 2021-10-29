import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import mechanicalsoup


url = "http://olympus.realpython.org/profiles/aphrodite"

# Open the url
page = urlopen(url)

# Return a sequence of bytes
html_bytes = page.read()

# Decode bytes to a string
html = html_bytes.decode("utf-8")

# Find and Extract Title
title_index = html.find("<title>")
print("Index", title_index)

# Star and End of Index of Title
start_index = title_index + len("<title>")

end_index = html.find("</title>")

title = html[start_index:end_index]

# A primer on Regular Expressions

found = re.findall("abc*c", "abc", re.IGNORECASE)


# Scrap a website
urls = "http://olympus.realpython.org/profiles/dionysus"

html_page = urlopen(urls)
html_text = html_page.read().decode('utf-8')

for string in ['Name:', 'Favorite Color:']:
    string_start_index = html_text.find(string)
    text_start_index = string_start_index + len(string)

    next_html_tag_offset = html_text[text_start_index:].find('<')
    text_end_index = text_start_index + next_html_tag_offset

    raw_text = html_text[text_start_index:text_end_index]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)


# Define Url, Open Url, Read&Decode Page, Bs4 Parse the HTML

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
image1, image2 = soup.find_all("img")
print(image1['src'])
print(soup.title)
print(soup.title.string)


urlb = 'http://olympus.realpython.org/profiles'
pageb = urlopen(urlb)
htmlb = pageb.read().decode('utf-8')
soup = BeautifulSoup(htmlb, "html.parser")

links = soup.find_all("a")
for i in links:
    prefix = urlb + i['href']
    print(prefix)


browser = mechanicalsoup.Browser()
url = "http://olympus.realpython.org/login"
page = browser.get(url)

print(page.soup)

