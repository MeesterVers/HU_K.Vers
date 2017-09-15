def swap (lijst):
	if len(lijst) > 1:
		# a = lijst[0]
		# b = lijst[1]
		# a,b = b,a
		lijst[0],lijst[1] = lijst[1],lijst[0]
		return lijst

lijst = [4, 0, 1, -2]
antwoord = swap(lijst)
print(antwoord)