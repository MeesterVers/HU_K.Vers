#Practice Exercise 1_4 (boolean expressions)
#1
a = 6
b = 7
antwoord_1 = 6.75 > a or 6.75 < b
print("1: 6.75 groter is dan a en kleiner b. \n" + str(antwoord_1) + "\n")

#2
inventaris = ['papier', 'nietjes', 'pennen']

voornaam = "Kadeem"
tussenvoegsel = "K.K."
achternaam = "Vers"

mijnnaam = ['voornaam', 'tussenvoegsel', 'achternaam']

antwoord_2 = len(inventaris) > len(mijnnaam)
print("2: De lengte van inventaris meer dan 5 keer zo groot is als de lengte van variabele mijnnaam. \n" + str(antwoord_2) + "\n")

#3
antwoord_3 = len(inventaris) == 0 or len(inventaris) > 10
print("3: De lijst inventaris leeg is, of juist meer dan 10 items bevat. \n" + str(antwoord_3) + "\n")
