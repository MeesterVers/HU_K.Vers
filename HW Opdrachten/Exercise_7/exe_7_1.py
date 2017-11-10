som = 0
aantal_getallen = 0

while True:
	getal = eval(input("Geef een getal: "))
	if getal != 0:
		som = getal + som
		aantal_getallen = aantal_getallen + 1
	elif getal == 0:
		break
print("Er zijn {} getallen ingevoerd, de som is: {}" .format(aantal_getallen, som))