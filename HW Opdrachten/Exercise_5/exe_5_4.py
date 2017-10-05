import datetime 

def get_lopers():
	infile = open('hardlopers.txt', 'r')
	lopers = infile.readlines()

	for loper in lopers:
		print(loper)

def lopers_gevens(naam):
	vandaag = datetime.datetime.today() 
	vandaag = vandaag.strftime("%a %d %b %Y %H:%M:%S")

	outfile = open('hardlopers.txt', 'a')
	outfile.write('{}, {}\n'.format(vandaag, naam))
	outfile.close()

while True:
	get_lopers()
	lopers_naam = input("\nWat is the lopers naam? ")

	if lopers_naam != "":
		lopers_gevens(lopers_naam)
	else:
		break