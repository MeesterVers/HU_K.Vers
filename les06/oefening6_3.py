gebruiker_zin = input("Voer zin in: ")
woorden = gebruiker_zin.split()

acroniem = ''
for woord in woorden:
	acroniem = acroniem + woord[0].upper()

print(acroniem)