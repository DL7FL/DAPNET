###############################################################################
# Philipp DL7FL mit unterstuezung von DH3RW (RWTH-AFU)
###############################################################################

import os
#import requests
#from requests.auth import HTTPBasicAuth
import dapnet
#import json
import logging # -> Logging vom Fehlermeldenung
import sys


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
callsign_list = ["dl7fl"]  # eins oder mehrere Emfaenger Rufzeichen
txgroup = "dl-he"  #  Sendergruppe zB. DL-all für alle Sender in Deutschland

##############################################################################
# Hauptprogramm
##############################################################################


dapnet.send(text, callsign_list, login, passwd, url)