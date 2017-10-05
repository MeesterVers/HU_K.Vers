infile = open('kaartnummer.txt', 'r')
regels = infile.readlines()
infile.close()

aantal_regels = len(regels)
hoogste_kaartnummer = 0

for regel in regels:
	regels_gesplits = regel.split(', ')
	kaart_nummer = int(regels_gesplits[0])

	if kaart_nummer > hoogste_kaartnummer:
		hoogste_kaartnummer = kaart_nummer

print("Deze file telt {} regels" .format(aantal_regels))
print("Het grooste kaartnummer is: {}" .format(hoogste_kaartnummer))