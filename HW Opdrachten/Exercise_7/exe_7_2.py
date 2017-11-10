while True:
	woord = input("Geef een string van vier letters: ")
	aantal_letters = len(woord)
	if aantal_letters != 4:
		print("{} heeft {} letters" .format(woord, aantal_letters))
	else:
		break
print("\nInlezen van correcte string: {} is geslaagd" .format(woord))