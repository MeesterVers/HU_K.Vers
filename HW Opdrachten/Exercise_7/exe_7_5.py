def namen():
	namen_dict = {}
	while True:
		naam = input("Voer naam in: ")
		if naam != "":
			if naam not in namen_dict:
				namen_dict[naam] = 1
			else:
				namen_dict[naam] = namen_dict[naam] + 1
		else:
			break
	print(namen_dict)
namen()