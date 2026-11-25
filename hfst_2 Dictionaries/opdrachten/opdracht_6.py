# Start de opdracht met onderstaande lijst.
fruitlijst = ["appel","doerian","banaan","doerian","appel","kers",
"kers","mango","appel","appel","kers","doerian","banaan",
"appel","appel","appel","appel","banaan","appel"]

fruiten = {}

for fruit in fruitlijst:
    if fruit not in fruiten:
        fruiten[fruit] = fruitlijst.count(fruit)

print(fruiten)