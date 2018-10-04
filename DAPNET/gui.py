from tkinter import *

# Die folgende Funktion soll ausgeführt werden, wenn
# der Benutzer den Button Klick mich anklickt
def button_action():
    entry_text = eingabefeld.get()
    if (entry_text == ""):
        welcome_label.config(text="Gib zuerst einen Namen ein.")
    else:
        entry_text = "Welcome " + entry_text + "!"
        welcome_label.config(text=entry_text)

fenster = Tk()
fenster.title("Ich warte auf eine Eingabe von dir.")

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

mainloop()