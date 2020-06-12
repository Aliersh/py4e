import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count=int(input('Enter count:'))
pos=int(input('Enter position:'))-1

while count>=0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print(url)
    url=tags[pos].get('href',None)
    count=count-1