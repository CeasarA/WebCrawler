import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
from PIL import Image
#io manages file-related in/out operations
import io
import pathlib
import tldextract
import hashlib
import csv


file = open('test_data.csv', newline='')
reader = csv.reader(file)
data_list = list(reader)
title  = data_list.pop(0)

urls = []
for x in data_list:
    urls.append(x[0])

print(urls)
links = []
# url = 'https://illinois.edu/fb/sec/229675'

# Extract domain
try:

    for u in urls:
        url_after_adding_https = 'http://' + u
        ext = tldextract.extract(url_after_adding_https)

        domain = ext.registered_domain

        # Make a request to url, It will return a response
        responses = requests.get(url_after_adding_https, verify=False)
        # Parse the response through BS4's html parser
        soup = BeautifulSoup(responses.text, "html.parser")

        # Extract all tags with 'img' in it
        raw_links = soup.find_all("img")

        # loop through raw links and process them
        for i in raw_links:
            link = i['src']
            if link.startswith("http"):
                links.append(link)
            else: 
                new_link = "https://" + domain + '/' + link
                links.append(new_link)
        
            print("Processed And Cleaned Links: ", links)

except Exception as e:
    print(e)

# Export data to a csv file
df = pd.DataFrame({"Links": links})
df.to_csv('test_data_images.csv', index=False, encoding='utf-8')

# Write and Download Images to a File
for x in links:
    image = requests.get(x).content
    #creates a byte object out of image_content and point the variable image_file to it
    image_file = io.BytesIO(image)
    image = Image.open(image_file).convert('RGB')
    print(image_file)
