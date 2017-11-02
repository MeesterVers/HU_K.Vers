import csv

#Er zit een kolomteskt in dus er komt een extra writer.writerow erin
with open('producten2.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter= ';')
    writer.writerow(('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))
    while True:
        artikelnummer = input('Wat is je artikelnummer: ')
        if artikelnummer == 'einde':
            break
        artikelcode = input('Voer artikelnummer: ')
        naam = input('Voer naam: ')
        voorraad = input('Aantal voorraad: ')
        prijs = input('Wat is prijs: ')

        writer.writerow((artikelnummer,artikelcode, naam,voorraad,prijs))