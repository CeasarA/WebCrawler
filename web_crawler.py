from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/aphrodite"

# Open the url
page = urlopen(url)

# Return a sequence of bytes
html_bytes = page.read()

# Decode bytes to a string
html = html_bytes.decode("utf-8")

# Find and Extract Title
title_index = html.find("<title>")
print(title_index)
