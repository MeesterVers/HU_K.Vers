try:
	bedrag = 4356
	aantal = eval(input('Voer het aantal in: '))
	if aantal < 0:
		print('Geen negatieve getallen')
	else:
		print(Bedrag/aantal)

except ZeroDivisionError:
	print('Delen door nul kan niet')
except NameError:
	print('Alleen cijfers')
except:
	print('onjuiste invoer')