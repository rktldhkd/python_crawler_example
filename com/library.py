# == 2. from urllib.request import urlopen
import urllib.request

url = "https://www.naver.com"
# == 2. hmtl = urlopen(url)
html = urllib.request.urlopen(url)

print(html.read())