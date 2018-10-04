################################################################################
# Philipp DL7FL mit unterstuezung von DH3RW (RWTH-AFU)
###############################################################################

import os
import logging # -> Logging vom Fehlermeldenung
import sys

import requests
from requests.auth import HTTPBasicAuth
import json

###############################################################################
# Funktionen definieren
###############################################################################

def send(text, callsign, login, passwd, url,txgroup="dl-he"): # mit json modul machen
	""" Sendet JASON-String zur Funkruf senden."""

	json_string =json.dumps({"text": text, "callSignNames": callsign, "transmitterGroupNames": [txgroup], "emergency":False})
	import pprint; pprint.pprint(json_string)
	response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd)) # Exception handling einbauen
	return response.status_code


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")
logger = logging.getLogger(sys.argv[0])

###############################################################################
#  Daten in Variablen Speichern
###############################################################################

# Konstante

#  DAPNET Benutzername
login = "dl7fl"  # Benutzername eintragen
#  DAPNET Passwort
passwd = "philipp87" # Passwort eintragen

url = 'http://www.hampager.de:8080/calls'  #  versenden uebers Internet Variable

text = "Dapnet-Script test  DL7FL"  #  Nachrichte ntext bis 80 Zeichen  eingebe
callsign_list = ["dl7fl" ]  # eins oder mehrere Emfaenger Rufzeichen
txgroup = "dl-he"  #  Sendergruppe zB. DL-all für alle Sender in Deutschland

##############################################################################
# Hauptprogramm
##############################################################################


send(text, callsign_list, login, passwd, url, txgroup)