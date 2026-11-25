# Vul onderstaande dictionary aan met behulp van input.
# relaties = {}

# relatie = input("Geef relatie tot persoon op: ")
# naam = input("Geef naam van persoon op: ")

# relaties[relatie] = naam

# print(relaties)

# relaties = {}

# while True:
#     relatie = input("Geef relatie tot persoon op: ")

#     if relatie == "STOP":
#         break

#     naam = input("Geef naam van persoon op: ")

#     if naam == "STOP":
#         break

#     relaties[relatie] = naam

# print(relaties)

relaties = {}

while True:
    relatie = input("Geef relatie tot persoon op: ")

    if relatie == "STOP":
        break

    naam = input("Geef naam van persoon op: ")

    if naam == "STOP":
        break

    if relatie in relaties:
        print("Kan relatie niet toevoegen, deze bestaat reeds")
    else:
        relaties[relatie] = naam

print(relaties)