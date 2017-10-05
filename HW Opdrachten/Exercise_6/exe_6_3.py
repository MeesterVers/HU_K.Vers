invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
getallen_lijst = invoer.split('-')
getallen_lijst.sort()
kleinste_getal = min(getallen_lijst)
grooste_getal = max(getallen_lijst)
aantal_getallen = len(getallen_lijst)
som_getallen = sum(getallen_lijst)
gemiddelde = som_getallen / aantal_getallen

print('Gesorteerde list van ints: {}' .format(getallen_lijst))
print('Groost getal: {}' .format(grooste_getal))
print('Kleinste getal: {}' .format(kleinste_getal))
print('Aantal getallen: {} en Som van de getallen: {}' .format(aantal_getallen, som_getallen))
print('Gemiddelde: {}' .format(gemiddelde))