import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
nlst=tree.findall(".//count")
print('Count:',len(nlst))
su=0

for item in nlst:
    num=int(item.text)
    su=su+num

print('Sum:',su)