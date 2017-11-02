import csv

with open('inloggen.csv', 'w', newline='') as myCSVFile:
	writer = csv.writer(myCSVFile, delimiter=';')

	while True:
		naam = input('naam ? ')
		if naam == 'einde':
			break

		voorletter = input('Voor letters ? ')
		gebdatum = input('Geboortedatum ? ')
		email = input('email ? ')

		writer.writerow((naam, voorletter, gebdatum, email))