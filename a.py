import urllib.request

url = 'http://checkip.amazonaws.com/'
f = urllib.request.urlopen(url)
ip=str(f.read().decode('utf-8')).strip()
print(ip)