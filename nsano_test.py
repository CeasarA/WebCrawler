import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
from PIL import Image
#io manages file-related in/out operations
import io
import pathlib
import hashlib

url = 'https://nsano.com/'

domain = urlparse(url=url).netloc
# Make a request to url, It will return a response

responses = requests.get(url)

# Parse the response through BS4's html parser
soup = BeautifulSoup(responses.text, "html.parser")

# Extract all tags with 'img' in it
raw_links = soup.find_all("img")

links = []
# loop through raw links and process them
for i in raw_links:
    link = i['src']
    if link.startswith("http"):
        links.append(link)
    else: 
        new_link = "https://" + domain + '/' + link
        links.append(new_link)

    print("Processed And Cleaned Links: ", links)

# Export data to a csv file
df = pd.DataFrame({"Links": links})
df.to_csv('images_from_nsano.csv', index=False, encoding='utf-8')

# Write and Download Images to a File
for x in links:
    image = requests.get(x).content
    #creates a byte object out of image_content and point the variable image_file to it
    image_file = io.BytesIO(image)
    image = Image.open(image_file).convert('RGB')
    print(image_file)

if __name__ == "__main__":
    print('main')