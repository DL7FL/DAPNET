###############################################################################################################
# Philipp DL7FL mit unterstuezung von DH3RW (RWTH-AFU)
##############################################################################################################

import requests
from requests.auth import HTTPBasicAuth

##############################################################################################################
#  Daten in Variablen Speichern
##############################################################################################################

text = ""  # Nachrichtentext bis 80 Zeichen  eingeben
callsign = ""  # Emfaenger Rufzeichen
txgroup = ""  # Sendergruppe zB. DL-all für alle Sender in Deutschland
login = ""  # DAPNET Benutzername
passwd = ""  # DAPNET Password
url = 'http://www.hampager.de:8080/calls'  # versenden uebers Internet

json_string = '''{"text": "''' + text + '''", "callSignNames": ["''' + callsign + '''"], "transmitterGroupNames": ["''' + txgroup + '''"], "emergency": false}'''
print(json_string)
response = requests.post(url, data=json_string, auth=HTTPBasicAuth(login, passwd))
print(response.status_code)
