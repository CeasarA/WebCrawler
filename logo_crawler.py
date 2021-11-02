import requests
import os
import re
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
import tldextract

def get_url(url, *args):
    if not url:
        return None

    if not url.startswith("https"):
        url = 'https://' + url    

    # Extract domain using tldextract
    ext = tldextract.extract(url)
    # Join the domain and suffix fields
    domain = ext.registered_domain
    print('domain: ', domain)

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
        return e

    links = []
    # loop through raw links and process them
    for i in raw_links:
        link = i.get('src', i.get('srcset'))
        if link.startswith("http"):
            links.append(link)
        else:
            new_link = "https://" + domain + '/' + link
            links.append(new_link)

    print("\n \n Processed Links", links)

    regex = re.compile(".*logo*")
    logo_links = list(filter(regex.match, links))
    print("\n \n Logo Links ", logo_links)

    try:
        logo = logo_links[0]
    except Exception as e:
        print("Error ", e)

    return logo_links


# Export data to a csv file
def convert_to_csv(get_url):
    # Structure the Links to be like a dict-like container for the Object

    try:
        df = pd.DataFrame({"Links": get_url})
        path = 'excel/' + 'logo_images.csv'
        df.to_csv(path, index=False, encoding='utf-8')
        return df
    except Exception as e:
        print("If using all scalar values, you must pass an index", e)


def download_image(links, pathname):
    # Write and Download Images to a File
    
    # Return None if no links are provided.
    if not links:
        return None

    # create path if it does not exist 
    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    for x in links:
        # image = requests.get(x).content
        response = requests.get(x, stream=True)
        # get file size
        print(response.headers)
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
        
        # Close the Connection Pool
        response.close()
    return links


# url = "https://www.verishop.com/ https://www.getequity.io/"


if __name__ == "__main__":
    url = "nsano.com"
    get_urr = get_url(url)
    print("Logo Link: ", get_urr)
    convert_to_csv(get_urr)
    path = 'images/' + url
    download_image(get_urr, path)