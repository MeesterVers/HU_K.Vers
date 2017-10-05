def gemiddelde(zin):
	zin_split = zin.split(" ")
	aantal_woorden = len(zin_split)
	aantal_letters = 0

	for woord in zin_split:
		for letter in woord:
			aantal_letters = aantal_letters + 1
	gemiddeld_lenght = aantal_letters // aantal_woorden
	return gemiddeld_lenght

gebruikers_zin = input('Voer een willekeurig zin in. \n')
lengte_zin = gemiddelde(gebruikers_zin)
print(lengte_zin)