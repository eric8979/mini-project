# Description
# Crawl Hackernews links with certain topic (first page)

import ssl
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

raw = urllib.request.urlopen('https://news.ycombinator.com').read()
soup = BeautifulSoup(raw, 'html.parser')
atags = soup.find_all('a', {'class': 'titlelink'})

newsData = []
for atag in atags:
    newsData.append((atag.get('href'), atag.get_text()))

for i in range(len(newsData)):
    print(str(i) + " : " + newsData[i][0] + " - " + newsData[i][1])
