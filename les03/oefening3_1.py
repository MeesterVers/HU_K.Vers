gebruiker_naam = input("Wat is uw naam? ")
gebruiker_leeftijd = eval(input("Wat is uw leeftijd? "))
message_succes = gebruiker_naam + ", je mag wel stemmen"
message_error = gebruiker_naam + ", je mag niet stemmen"

if gebruiker_leeftijd < 18:
	print(message_error)
else:
	print(message_succes)