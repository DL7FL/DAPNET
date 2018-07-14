################################################################################
# Philipp DL7FL mit unterstuezung von DH3RW (RWTH-AFU)
###############################################################################

import os
import dapnet
import logging # -> Logging vom Fehlermeldenung
import sys
from tkinter import *


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s;%(levelname)s;%(message)s")
logger = logging.getLogger(sys.argv[0])

###############################################################################
#  Daten in Variablen Speichern
###############################################################################
# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button Klick mich anklickt
def button_action():
    entry_text = eingabefeld.get()
    if (entry_text == ""):
        welcome_label.config(text="Gib zuerst einen Namen ein.")
    else:
        entry_text = "Welcome " + entry_text + "!"
        welcome_label.config(text=entry_text)

# Konstante

login = os.getenv('DAPNET_Benutzer') #  DAPNET Benutzername aus Umgebungsvariablen in Pysharm os.getenv oder config datei yaml / json
passwd = os.getenv('DAPNET_Passwort')  #  DAPNET Passwort aus Umgebungsvariablen config.py

url = 'http://www.hampager.de:8080/calls'  #  versenden uebers Internet Variable

text = "Dapnet test DL7FL"  #  Nachrichte ntext bis 80 Zeichen  eingebe
callsign_list = ["dl7fl"]  # eins oder mehrere Emfaenger Rufzeichen DL4FLY
txgroup = "dl-he"  #  Sendergruppe zB. DL-all für alle Sender in Deutschland

#############################
#   GUI
#############################
fenster = Tk()
fenster.title("DAPNET Funkruf")

# Anweisungs-Label
my_label = Label(fenster, text="Gib deinen Namen ein: ")

# In diesem Label wird nach dem Klick auf den Button der Benutzer
# mit seinem eingegebenen Namen begrüsst.
welcome_label = Label(fenster)

# Hier kann der Benutzer eine Eingabe machen
eingabefeld = Entry(fenster, bd=5, width=40)

welcom_button = Button(fenster, text="Klick me", command=button_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)


# Nun fügen wir die Komponenten unserem Fenster hinzu
my_label.grid(row = 0, column = 0)
eingabefeld.grid(row = 0, column = 1)
welcom_button.grid(row = 1, column = 0)
exit_button.grid(row = 1, column = 1)
welcome_label.grid(row = 2, column = 0, columnspan = 2)

##############################################################################
# Hauptprogramm
##############################################################################


dapnet.send(text, callsign_list, login, passwd, url, txgroup)

mainloop()