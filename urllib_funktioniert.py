import requests

Webseite = "http://google.com"
t = requests.urlopen (Webseite).read()

print(t)
