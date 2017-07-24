import urllib.request
import re

urls=["http://google.com","http://reddit.com"]

i=0

these_regex="<title>(.+?)</title>"
#pattern=re.compile(these_regex)

while(i<len(urls)):
        htmlfile=urllib.request.urlopen(urls[i])
        htmltext=htmlfile.read()
        titles=re.findall(these_regex,htmltext)
        print(titles)
        i+=1