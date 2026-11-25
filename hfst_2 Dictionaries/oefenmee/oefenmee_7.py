# Start de oefen mee met onderstaande dictionary.
gasten = { # Sleutel is naam, waarde is job.
    "Jan":     "reporter",
    "Piet":    "acteur",
    "Joris":   "regisseur",
    "Korneel": "scenarist"
}

while True:
    naam = input("Geef naam Gebruiker: ")
    if naam in gasten:
        print(f"welkom {naam} {gasten[naam]}. Kom binnen.")
        gasten.pop(naam)

    else:
        print(f"De naam{naam} staat niet op de lijst.")
    
        if naam == "STOP":
            break
