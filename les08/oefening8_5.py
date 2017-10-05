import random

def diceprob(invoersom):
	aantalworpen = 0
	aantalworpen_ingevoerd = 0

	while aantalworpen_ingevoerd < 100:
		aantalogen1 = random.randrange(1, 7)
		aantalogen2 = random.randrange(1, 7)
		som = aantalogen1 + aantalogen2

		if invoersom == som:
			aantalworpen_ingevoerd = aantalworpen_ingevoerd + 1
		aantalworpen = aantalworpen + 1
	print('het aaantal benodige worpen is {}' .format(aantalworpen))

somaantalogen = eval(input('Hoe groot is de som: '))
diceprob(somaantalogen)