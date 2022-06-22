# Crawl Hackernews links with certain topic (first page) (regex)
import socket
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

# ---------------------------------------

# mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysocket.connect(('news.ycombinator.com', 443))
# request = 'GET https://news.ycombinator.com HTTP/1.0\n\n'.encode()
# mysocket.send(request)

# while True:
#     try:
#         raw = mysocket.recv(1024)
#         if len(raw) < 1:
#             break
#         print(raw.decode())
#     except:
#         print('failed to receive info')
#         break

# mysocket.close()
