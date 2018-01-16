"""Funtionen zu Dapnet-Funkrufe versenden."""

import requests
from requests.auth import HTTPBasicAuth

###############################################################################
# Funktionen definieren
###############################################################################

def send(text, callsign, txgroup, login, passwd, url): # mit json modul machen
	""" Sendet JASON-String zur Funkruf senden."""
	json_string = '''{"text": "''' + text + '''", "callSignNames": ["''' + callsign + '''"], "transmitterGroupNames": ["''' + txgroup + '''"], "emergency": false}'''
	# print(json_string)
	response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd)) # Exception handling einbauen
	statuscode =(response.status_code)
	return statuscode# return von der Funktion


def single_callsign(callsign_list): #  Rufzeichen vereinzelt und ruft mit jedem Rufzeichen die Send Funktion auf.
	"""Zerlegt die callsign_list in einzelne callsign"""
	for callsign in callsign_list:
		send(text, callsign, txgroup, login, passwd, url)
	return