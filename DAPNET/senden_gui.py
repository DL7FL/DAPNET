################################################################################
# Philipp DL7FL mit unterstuezung von DH3RW (RWTH-AFU)
###############################################################################

import os
import dapnet
import logging # -> Logging vom Fehlermeldenung
import sys
from tkinter import *

# Logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")
logger = logging.getLogger(sys.argv[0])

# GUI Funktionen

# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button Senden anklickt
def button_senden():
    entry_text = eingabefeld_nachricht.get()
    if (entry_text == ""):
        status_label.config(text="Gib zuerst eine Nachricht ein.")
    else:
        text_nachricht = entry_text + "test"
        status_label.config(text=text_nachricht)

 ###############################################################################
 #  Daten in Variablen Speichern
 ###############################################################################

# Konstante

login = os.getenv('DAPNET_Benutzer') #  DAPNET Benutzername aus Umgebungsvariablen in Pysharm os.getenv oder config datei yaml / json
passwd = os.getenv('DAPNET_Passwort')  #  DAPNET Passwort aus Umgebungsvariablen config.py

url = 'http://www.hampager.de:8080/calls'  #  versenden uebers Internet Variable

#text = "Dapnet test DL7FL"  #  Nachrichte ntext bis 80 Zeichen  eingebe
callsign_list = ["dl7fl"]  # eins oder mehrere Emfaenger Rufzeichen DL4FLY
txgroup = "dl-he"  #  Sendergruppe zB. DL-all für alle Sender in Deutschland

#############################
#   GUI
#############################
fenster = Tk()
fenster.title("DAPNET Funkruf")

# Nachricht-Label
nachricht_label = Label(fenster, text="Nachricht eingeben: ")

# In diesem Label wird nach dem Klick auf den Button der Status ausgegeben
status_label = Label(fenster)

# Eingabefeld für Nachricht
eingabefeld_nachricht = Entry(fenster, bd=5, width=80)

# Sende Button ruft Funktion button_senden auf
senden_button = Button(fenster, text="Senden", command=button_senden())
# Button zum Programm beenden
exit_button = Button(fenster, text="Beenden", command=fenster.quit)


# Komponenten Anordnungim Fenster
nachricht_label.grid(row = 0, column = 0)
eingabefeld_nachricht.grid(row = 0, column = 1)

senden_button.grid(row = 1, column = 0)
exit_button.grid(row = 1, column = 1)

status_label.grid(row = 2, column = 0, columnspan = 2)

##############################################################################
# Hauptprogramm
##############################################################################


#dapnet.send(text, callsign_list, login, passwd, url, txgroup)

mainloop()