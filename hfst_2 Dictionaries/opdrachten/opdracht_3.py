# Start met onderstaande dictionary.
database = { # Sleutel = naam, waarde = wachtwoord
    "Jan": "FkeHsne569*",
    "Piet": "KsnOmd727^",
    "Joris": "DneSje439&",
    "Korneel": "MdsSnz863*"
}

naam = input("Wie wilt inloggen: ")

if naam not in database:
    print(naam, "bestaat niet in de database.")
else:
    wachtwoord = input("Geef wachtwoord op van " + naam + ": ")

    if wachtwoord == database[naam]:
        print("Welkom", naam + "!")
    else:
        print("Wachtwoord incorrect.")
