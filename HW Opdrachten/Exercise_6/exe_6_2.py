zin = input('Voer een zin in met tenminste 10 woorden: \n')
lijst = zin.split(' ')
vier_letter_lijst = []

for woord in lijst:
	if len(woord) == 4:
		vier_letter_lijst.append(woord)

print('\n')
print('De orginele woordenlijst: \n {}' .format(lijst))
print('\n')
print('De lijst met vier letterige woorden: \n {}' .format(vier_letter_lijst))