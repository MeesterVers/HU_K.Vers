s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = ["a", "e", "i", "o", "u"]

for letter in s:
	if letter in klinkers:
		print(letter)