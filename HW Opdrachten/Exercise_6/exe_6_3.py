invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
getallen_lijst = invoer.split('-')
getallen_lijst.sort()
getallen_lijst_int = list(map(int, getallen_lijst))

kleinste_getal = min(getallen_lijst_int)
grooste_getal = max(getallen_lijst_int)
aantal_getallen = len(getallen_lijst_int)
som_getallen = sum(getallen_lijst_int)
gemiddelde = som_getallen / aantal_getallen

print('Gesorteerde list van ints: {}' .format(getallen_lijst_int))
print('Groost getal: {}' .format(grooste_getal))
print('Kleinste getal: {}' .format(kleinste_getal))
print('Aantal getallen: {} en Som van de getallen: {}' .format(aantal_getallen, som_getallen))
print('Gemiddelde: {}' .format(gemiddelde))