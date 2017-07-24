import urllib.request
import re

urls = ['http://google.com' , 'http://cnn.com']

i=0

while i < len(urls):
    htmltext = urllib.request.urlopen(urls[i]).read()
    titles = re.findall(r'<.*?','<title>(.+?)</title>', str(htmltext))
    print(titles)
    i+= 1
