tafels = {
    'Tafel 1': 45.50,
    'Tafel 3': 22.00,
    'Tafel 4': 87.10
}


while True:
    Tafelnaam = input("Geef tafelnaam in: ")
    wat = input("Bestellen of afrekenen? ")

    if wat == "Bestellen": 
        Bedrag = int(input("Wat is het bedrag van de nieuwe bestelling? "))
        if Tafelnaam in tafels:
            tafels[Tafelnaam] += Bedrag
        else:
            tafels[Tafelnaam] = Bedrag
        print(tafels[Tafelnaam], Bedrag)
    elif wat == "Afrekenen":
        if Tafelnaam in tafels:
            print(tafels[Tafelnaam] )
            tafels.pop(Tafelnaam)
        else:
            tafels[Tafelnaam] = "Er is geen openstaande rekening voor deze tafel!"

        print(tafels)
        
        break
