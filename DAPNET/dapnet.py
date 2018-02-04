
import requests
from requests.auth import HTTPBasicAuth
import json

###############################################################################
# Funktionen definieren
###############################################################################

def send(text, callsign, login, passwd, url,txgroup="dl-he"): # mit json modul machen
	""" Sendet JASON-String zur Funkruf senden."""

	json_string =json.dumps({"text": text, "callSignNames": callsign, "transmitterGroupNames": [txgroup], "emergency": False})
	import pprint; pprint.pprint(json_string)
	response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd)) # Exception handling einbauen
	return response.status_code


def single_callsign(callsign_list): #  Rufzeichen vereinzelt und ruft mit jedem Rufzeichen die Send Funktion auf.
	"""Zerlegt die callsign_list in einzelne callsign"""
	for callsign in callsign_list:
		send(text, callsign, login, passwd, url)
	return
