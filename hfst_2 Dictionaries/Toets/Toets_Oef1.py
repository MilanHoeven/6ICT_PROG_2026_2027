

gebruikers = {
    'hendrik.clijsters': 'SteDri39',
    'spma300906': 'MauSpi21',
    'bija080714': 'BirJal08',
    'johan.colson': 'ColHan44',
    'momo250308': 'SerRam26'
}
punt = "."
uitroepteken = "!"

for sleutel,waarde in gebruikers.items():
    if punt not in sleutel:
        print(f"{sleutel}!" )

print(gebruikers)
    