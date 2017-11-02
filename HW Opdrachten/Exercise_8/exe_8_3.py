def code(invoerstring):
	nieuwestring = ''

	for letter in invoerstring:
		nieuweASCII = ord(letter) + 3
		nieuwekar = chr(nieuweASCII)
		nieuwestring += nieuwekar
	return nieuwestring


naam = input('Wat is uw naam? ')
beginstaion = input('Van welke station vertrekt u? ')
eindstation = input('Bij welke station gaat u uitstappen? ')
invoerstring = naam + beginstaion + eindstation

print()
print(invoerstring)
print(code(invoerstring))