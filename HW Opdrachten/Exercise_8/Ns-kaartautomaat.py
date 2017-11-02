stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

# begin station inlezen functie
def inlezen_beginstation(stations):
	beginstation = input('\nVoer uw beginstation in: ')
	
	while beginstation not in stations:
		print('Deze trein vertrekt niet van {}' .format(beginstation))
		beginstation = input('Voer een andere beginstation in: ')
	return beginstation
# begin station inlezen functie

# eind station inlezen functie
def inlezen_eindstation(stations, beginstation):
	eindstation = input('Voer uw eindstation in: ')

	while eindstation not in stations:
		print('Deze trein komt niet in {}' .format(eindstation))
		eindstation = input('Voer uw eindstation in: ')

	while stations.index(eindstation) < stations.index(beginstation):
		print('De trein is het station {} al voorbij' .format(eindstation))
		eindstation = input('Voer een andere eindstation in: ')
	return eindstation
# eind station inlezen functie

# Omroep reis functie
def omroepen_reis(stations, beginstation, eindstation):
	nummer_b_orgineel = stations.index(beginstation)
	nummer_b = stations.index(beginstation) + 1
	nummer_e_orgineel = stations.index(eindstation)
	nummer_e = stations.index(eindstation) + 1
	afstand = nummer_e - nummer_b
	prijs = 5 * afstand
		
	print('\nHet beginstation {} is het {}e station in het traject.' .format(beginstation, nummer_b))
	print('Het eindstation {} is het {}e station in het traject.' .format(eindstation, nummer_e))
	print('De afstand bedraagt {} station(s)' .format(afstand))
	print('De prijs van het kaartje is {} euro. \n' .format(prijs))


	print('Jij stapt in de trein in: {}' .format(beginstation))
	for tussen_stop_index in range(nummer_b, nummer_e_orgineel):
		tussen_stop_naam = stations[tussen_stop_index]
		print(' - {}' .format(tussen_stop_naam))
	print('Jij stapt uit in: {}' .format(eindstation))
# Omroep reis functie

beginstation = inlezen_beginstation(stations) 
eindstation = inlezen_eindstation(stations, beginstation) 
omroepen_reis(stations, beginstation, eindstation)