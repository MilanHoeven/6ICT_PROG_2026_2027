dambord_2D = [
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W'],
    ['W', 'Z', 'W', 'Z', 'W', 'Z'],
    ['Z', 'W', 'Z', 'W', 'Z', 'W']]

rij = int(input("geef een rij op: "))
kolom = int(input("geef een kolom op: "))

if rij <= 5 and kolom <= 5:
    nieuw = dambord_2D[rij][kolom]
    print(nieuw)
else:
    print("waarde te groot")