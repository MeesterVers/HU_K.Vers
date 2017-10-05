woord = input('Voer een woord in: ')

for letter in woord:
	asc = ord(letter)
	print('{} {} {:x} {:b}' .format(letter, asc, asc, asc))