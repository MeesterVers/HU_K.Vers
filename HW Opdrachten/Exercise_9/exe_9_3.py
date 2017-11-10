import csv

hoogste_score = 0
datum = 0
naam = 0
with open('gamers.csv', newline='') as myCSVFile:
	gamers = csv.reader(myCSVFile, delimiter=';')
	for row in gamers:
		if int(row[2]) > hoogste_score:
			hoogste_score = int(row[2])
			datum = row[1]
			naam = row[0]
print("De hoogste score is: {} op {} behaald door {}" .format(hoogste_score, datum, naam))