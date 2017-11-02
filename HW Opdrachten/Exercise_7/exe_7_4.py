def ticker():
	infile = open('ticker.txt', 'r')
	regels = infile.readlines()
	infile.close()

	tickerdict = {}

	for regel in regels:
		ticker_regel = regel.split(':')
		sleutel = ticker_regel[0]
		waarde = ticker_regel[1].strip()
		tickerdict[sleutel] = waarde
	return tickerdict

tickerbestand = ticker()
bedrijfnaam = input('Geef bedrijf: ')
for naam in tickerbestand:
	if naam == bedrijfnaam:
		print(tickerbestand[naam])

code = input('Geef code: ')
for naam in tickerbestand:
	if code == tickerbestand[naam]:
		print(naam)