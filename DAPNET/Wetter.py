### Nur Wettermeldung vom BBK abrufen.

import json
import requests

url = "https://warnung.bund.de/bbk.dwd/unwetter.json"
unwetterjson = requests.get(url)
unwetterwarnunglist = json.loads(unwetterjson.text)

print(type(unwetterwarnunglist))
print(type(unwetterwarnunglist[0]))

for unwetterwarnung in unwetterwarnunglist:
    print(unwetterwarnung)

