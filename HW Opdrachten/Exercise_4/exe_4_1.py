def som (getal1, getal2, getal3):
	getallen = [getal1, getal2, getal3]
	som_getallen = sum(getallen)
	return som_getallen

getal1 = eval(input('Getal 1: '))
getal2 = eval(input('Getal 2: '))
getal3 = eval(input('Getal 3: '))

antwoord = som(getal1, getal2, getal3)
print(antwoord)