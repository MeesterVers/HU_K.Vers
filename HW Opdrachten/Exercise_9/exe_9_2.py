import csv
import datetime

with open('inloggen.csv', 'w', newline='') as myCSVFile:
	writer = csv.writer(myCSVFile, delimiter=';')

	while True:
		naam = input('Wat is je achternaam: ')
		if naam == 'einde':
			break

		voorletter = input('Wat zijn je voorletters: ')
		gebdatum = input('Wat is je geboortedatum: ')
		email = input('Wat is je email adres: ')
		vandaag = datetime.datetime.today() 
		vandaag = vandaag.strftime("%a %d %b %Y %H:%M:%S")

		writer.writerow((vandaag, naam, voorletter, gebdatum, email))