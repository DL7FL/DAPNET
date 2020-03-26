import requests
from requests.auth import HTTPBasicAuth
import json

## Hachathon HamHack

###############################################################################
# Funktionen definieren
###############################################################################

def send(text, callsign, login, passwd, url,txgroup="dl-he", emergency = False): # mit json modul machen
	""" Sendet JASON-String zur Funkruf senden."""

	json_string =json.dumps({"text": text, "callSignNames": callsign, "transmitterGroupNames": [txgroup], "emergency": emergency})
	import pprint; pprint.pprint(json_string)
	response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd)) # Exception handling einbauen
	return response.status_code

