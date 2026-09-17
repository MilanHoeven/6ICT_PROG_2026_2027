telefoonboek = {
    "Jan": "282929892",
    "Piet": "18181881",
    "Kapper Korneel": "28373883"
}

naam = input("geef een naam: ")

if naam in telefoonboek:
    print(telefoonboek[naam] )
else:
    print("Deze bestaat niet :(")