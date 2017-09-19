# standaard tarief funtie start
def standaardtarief(afstandKM):
	trein_rit = 0.80
	vastbedrag = 0

	if afstandKM > 50:
		trein_rit = 0.60
		vastbedrag = 15.0
		totaal = afstandKM * trein_rit + vastbedrag
		return totaal

	if afstandKM < 50 and afstandKM > 0:
		totaal = afstandKM * trein_rit
		return totaal

	if afstandKM <= 0:
		totaal = trein_rit * 0
		return totaal
# standaard tarief funtie einde

# ritprijs start
def ritprijs(leeftijd, weekendrit, afstandKM):
	sub_totaal = standaardtarief(afstandKM)
	
	if weekendrit == "false":
		if leeftijd < 12 or leeftijd >= 65:
			korting = sub_totaal / 10 * 3
			totaal = sub_totaal - korting
			return totaal
		else:
			totaal = sub_totaal
			return totaal

	if weekendrit == "true":
		if leeftijd < 12 or leeftijd >= 65:
			korting = sub_totaal / 10 * 3.5
			totaal = sub_totaal - korting
			return totaal
		else:
			korting = sub_totaal / 10 * 4
			totaal = sub_totaal - korting
			return totaal
# ritprijs einde


# hoofdprogramma
afstandKM = eval(input("Hoeveel kilomter is er gereizd? "))
weekendrit = input("Is het weekend? ")
leeftijd = eval(input("Wat is de reizigers leeftijd? "))

bedrag = ritprijs(leeftijd, weekendrit, afstandKM)

message = "Het te betalen bedrag is: " + str(bedrag) + " Euro"
print(message)