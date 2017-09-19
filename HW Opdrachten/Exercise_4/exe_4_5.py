def kwadraten_som(grondgetallen):
	som = 0

	for grondgetal in grondgetallen:
		if grondgetal > 0:
			som = som + grondgetal * grondgetal
	return som

lijst = [4, 5, 3, -81]
antwoord = kwadraten_som(lijst)
print(antwoord)