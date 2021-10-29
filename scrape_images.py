import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd

url = 'https://nsano.com/'

# Extract domain
domain = urlparse(url=url).netloc

# Make a request to url, It will return a response
responses = requests.get(url)

# Parse the response through BS4's html parser
soup = BeautifulSoup(responses.text, "html.parser")

# Extract all tags with 'img' in it
raw_links = soup.find_all("img")

# loop through raw links and process them
links = []
for i in raw_links:
    link = i['src']
    if link.startswith("http"):
        links.append(link)
    else: 
        new_link = "https://" + domain + '/' + link
        links.append(new_link)


print("Processed And Cleaned Links: ", links)

# Write and Dwonload Images to a File
for x in links:
    image = requests.get(x).content
    # print(image)
    break

# Export data to a csv file
df = pd.DataFrame({"Links": links})
df.to_csv('images_from_nsano.csv', index=False, encoding='utf-8')