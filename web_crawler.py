import re
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
print("Index", title_index)

# Star and End of Index of Title
start_index = title_index + len("<title>")

end_index = html.find("</title>")

title = html[start_index:end_index]
print("Title: ", title)

# A primer on Regular Expressions

found = re.findall("abc*c", "abc")
print(found)