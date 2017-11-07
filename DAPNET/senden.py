###############################################################################
# Philipp DL7FL mit unterstuezung von DH3RW (RWTH-AFU)
###############################################################################

import requests
from requests.auth import HTTPBasicAuth

###############################################################################
#  Daten in Variablen Speichern
###############################################################################

# Konstante

login = ""  # DAPNET Benutzername
passwd = ""  # DAPNET Password
url = 'http://www.hampager.de:8080/calls'  # versenden uebers Internet

text = ""  # Nachrichtentext bis 80 Zeichen  eingeben
rufzeichen = ["DL7FL","DL7FL"]  #  # eins oder mehrere Emfaenger Rufzeichen
txgroup = "dl-he"  # Sendergruppe zB. DL-all für alle Sender in Deutschland


###############################################################################
# Funktionen definieren
###############################################################################

def senden(text, callsign, txgroup, login, passwd, url):
	# print(callsign)
	json_string = '''{"text": "''' + text + '''", "callSignNames": ["''' + callsign + '''"], "transmitterGroupNames": ["''' + txgroup + '''"], "emergency": false}'''
	# print(json_string)
	response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd))
	print(response.status_code)


def Rufzeichen_vereinzeln(rufzeichen):  #  Rufzeichen vereinzelt und ruft mit jedem Rufzeichen die Senden Funktion auf.
	for callsign in rufzeichen:
		# print(callsign)

		senden(text, callsign, txgroup, login, passwd, url)


Rufzeichen_vereinzeln(rufzeichen)