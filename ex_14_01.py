import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

info=json.loads(data)
cinfo=info['comments'] #For looping in comments list
print('Count:',len(cinfo))
su=0

for item in cinfo:
    num=int(item['count'])
    su=su+num

print('Sum:',su)