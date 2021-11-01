import requests
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import pandas as pd
from tqdm import tqdm


def get_url(url):
    domain = urlparse(url=url).netloc
    print('domain', domain)
    raw_links = []
    # Try and make a request to url, It will return a response
    try:
        responses = requests.get(url)
        # Parse the response through BS4's html parser
        soup = BeautifulSoup(responses.text, "html.parser")

        # Extract all tags with 'img' in it
        raw_links = soup.find_all("img")
        print('\n \n raw_links', raw_links)
    except Exception as e:
        print("Error", e)

    links = []
    # loop through raw links and process them
    for i in raw_links:
        link = i['src']
        if link.startswith("http"):
            links.append(link)
        else: 
            new_link = "https://" + domain + '/' + link
            links.append(new_link)
    print("\n \n Processed Links", links)

    regex = re.compile(".*png")
    new_links = list(filter(regex.match, links))
    print("\n \n Logo Links ", new_links)

    return links


# Export data to a csv file
def convert_to_csv(get_url):
    # Structure the Links to be like a dict-like container for the Object
    df = pd.DataFrame({"Links": get_url})

    df.to_csv('images_from_nsano.csv', index=False, encoding='utf-8')

    return df


def download_image(links, pathname):
    # Write and Download Images to a File

    # create path if it does not exist 
    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    for x in links:
        image = requests.get(x).content
        response = requests.get(x, stream=True)
        # get file size
        file_size = int(response.headers.get("Content-Length", 0))
        # define file path
        file_name = os.path.join(pathname, x.split("/")[-1])
        # progress bar to change the units to bytes
        progress = tqdm(response.iter_content(1024), f"Downloading {file_name}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
        # open the 
        with open(file_name, 'wb') as f:
            for data in progress.iterable:
                f.write(data)
                # Update download progress
                progress.update(len(data))

    return links


url = "https://www.kwidex.com/"
get_urr = get_url(url)
# convert_to_csv(get_urr)
# download_image(get_urr, 'images')

if __name__ == "main":
    url = "https://nsano.com/"
    get_urr = get_url(url)
    print("all urls", get_urr)