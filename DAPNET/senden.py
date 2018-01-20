###############################################################################
# Philipp DL7FL mit unterstuezung von DH3RW (RWTH-AFU)
###############################################################################

import os
import sys
import requests
from requests.auth import HTTPBasicAuth
import dapnet
import json
import logging # -> Logging vom Fehlermeldenung


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")
logger = logging.getLogger(sys.argv[0])

###############################################################################
#  Daten in Variablen Speichern
###############################################################################

# Konstante

login = os.getenv('DAPNET_Benutzer') #  DAPNET Benutzername aus Umgebungsvariablen in Pysharm os.getenv oder config datei
passwd = os.getenv('DAPNET_Passwort')  #  DAPNET Passwort aus Umgebungsvariablen


url = 'http://www.hampager.de:8080/calls'  #  versenden uebers Internet Variable

text = "test cccffm"  #  Nachrichte ntext bis 80 Zeichen  eingeben
callsign_list = ["dl7fl","DH2fg"]  # eins oder mehrere Emfaenger Rufzeichen
txgroup = "dl-he"  #  Sendergruppe zB. DL-all für alle Sender in Deutschland

###############################################################################
# Funktionen definieren
###############################################################################
'''
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

'''
##############################################################################
# Hauptprogramm
##############################################################################

#single_callsign(callsign_list)
dapnet.send(text, callsign_list, login, passwd, url)