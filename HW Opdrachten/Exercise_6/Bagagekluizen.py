def toon_aantal_kluizen_vrij():
	infile = open('kluizen.txt', 'r')
	kluizen = infile.readlines()
	aantal_kluizen = len(kluizen)
	print(aantal_kluizen)
#einde aantal kluizen vrij

def nieuwe_kluis():
	lijst_totaal_kluisnummers = ['1','2','3','4','5','6','7','8','9','10','11','12']
	infile = open('kluizen.txt', 'r')
	kluizen = infile.readlines()

	for kluis in kluizen:
		nummer_code_splits = kluis.split(";")
		for kluisnummer in nummer_code_splits:
			if kluisnummer in lijst_totaal_kluisnummers:
				lijst_totaal_kluisnummers.remove(kluisnummer)

	if lijst_totaal_kluisnummers != "":
		code = input("Voer uw kluiscode in: ")
		code_confirm = input("Voer uw kluiscode nog een keer in: ")
		while code != code_confirm:
			code = input("Voer uw kluiscode in: ")
			code_confirm = input("Voer uw kluiscode nog een keer in: ")
		
		if code == code_confirm:
			kluisnummer = lijst_totaal_kluisnummers[0]
			save_kluis = open('kluizen.txt', 'a')
			save_kluis.write('{};{}\n'.format(kluisnummer, code))
			save_kluis.close()
			print("\nKluis succesvol opgeslagen.\nUw kluisnummer is: {} Vergeet aub uw code niet." .format(kluisnummer))
# einde nieuwe kluis

def kluis_openen():
	kluisnummer = eval(input("Kies uw kluisnummer: "))
	kluiscode = input("Voer aub uw kluiscode in: ")
	message = 0
	invoer_kluis = str(kluisnummer) + ";" + kluiscode
	infile = open('kluizen.txt', 'r')
	kluizen = infile.readlines()

	for kluis in kluizen:
		if invoer_kluis in kluis:
			message = "Dat is een goede combinatie de kluis is open."
			break
		else:
			message = "Dat is een foutieve combinatie."
	print(message)
# eninde kluis open

kluis_openen()