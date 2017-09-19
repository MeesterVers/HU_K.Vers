gebruiker_naam = input("Wat is uw naam? ")
passpoort = input("Heeft u een Nederlandse passpoort? ")
gebruiker_leeftijd = eval(input("Wat is uw leeftijd? "))

message_succes = gebruiker_naam + ", je mag wel stemmen"
message_error = gebruiker_naam + ", je mag niet stemmen"

if gebruiker_leeftijd >= 18 and passpoort == "ja":
	print(message_succes)
else:
	print(message_error)