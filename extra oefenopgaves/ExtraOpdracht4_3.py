def eindbedrag(bedrag, percentage):
	bedrag = bedrag + percentage * bedrag / 100
	return  bedrag

bedrag = eval(input('Geen een bedrag: '))
