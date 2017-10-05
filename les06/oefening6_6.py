def pixels(list):
	aantal_rijen = len(list)
	aantal_kolommen =  len(list[0])
	aantal_postieve = 0

	for rij in range(aantal_rijen):
		for kolom in range(aantal_kolommen):
			if list[rij][kolom] > 0:
				aantal_postieve = aantal_postieve + 1
	return aantal_postieve

lst = [[0, 156, 0, 0], [34, 0, 0, 0], [23, 123, 0, 34]]
print (pixels(lst))