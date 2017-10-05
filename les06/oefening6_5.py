table1 = [[4,7,2,5], [5,1,9,2], [8,3,6,6]]

aantalrijen = len(table1)
aantalkolommen = len(table1[0])

for rij in range(aantalrijen):
	for kolom in range(aantalkolommen):
		print(table1[rij][kolom], end = ' ')
	print()