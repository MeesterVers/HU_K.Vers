getallenrij = [2, 4, 6, 8, 10, 9, 7]
ingevoerd_getal = eval(input("Zoek getal: "))
gevonden = False

for getal in getallenrij:
	if ingevoerd_getal == getal:
		gevonden = True

if gevonden == True:
	print(str(ingevoerd_getal) + " Zit in het getallenrij")
else:
	print(str(ingevoerd_getal) + " Zit niet het getallenrij")
