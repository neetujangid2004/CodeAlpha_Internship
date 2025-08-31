# Scrape the title of a fixed webpage

import requests
import re

url = "https://github.com"

response = requests.get(url)
html = response.text

match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE)

if match:
    title = match.group(1)
    with open("/home/neetu/Documents/Intership/CodeAlpha_Internship/CodeAlph_TaskAutomation/web_title.txt", "w") as f:
        f.write(title)

    print("Title saved:", title)
else:
    print("No title found on the page")