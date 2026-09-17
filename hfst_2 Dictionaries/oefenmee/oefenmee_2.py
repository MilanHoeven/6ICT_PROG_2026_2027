# Start de oefen mee met onderstaande dictionary.
fruitmand = { # Sleutel is fruit, waarde is aantal
    "appel": 5,
    "banaan": 3,
    "kers": 50
}
# niveau 1:
# fruit = "banaan"
# print(fruitmand[fruit])

# nieveau2:
# nieuw_fruit = "mango"
# nieuw_aantal = 1
# fruitmand[nieuw_fruit] = 1

# niveau3
# fruit = "banaan"
# nieuw_aantal = 8
# fruitmand[fruit] = 8

# verlaag_met = 43
# fruitmand["kers"] = fruitmand["kers"] - 43
# print(fruitmand)

terugleggen_fruit = "kers"
fruitmand.pop("kers")
print(fruitmand)
