def seizoen(maand):
	if maand == 12 or maand == 1 or maand == 2:
		resultaat = 'Winter'
	elif maand >= 3 and maand <= 5:
		resultaat = 'Lente'
	elif maand >= 6 and maand <= 8:
		resultaat = 'Zomer'
	elif maand >= 9 and maand <= 11:
		resultaat = 'Herfst'
	else:
		resultaat = 'Ooops dat is geen maand'
	return resultaat

gekozen_maand = eval(input('Kies een maand getal dus tussen 1 en 12: '))
print(seizoen(gekozen_maand))