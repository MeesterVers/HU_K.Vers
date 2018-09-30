# Schrijf (en test) de functie som() die 1 parameter heeft: getallenLijst. Ga ervan uit dat dit een list is met integers. De return-waarde van de functie moet de som (optelling) van de getallen in de lijst zijn! Tip: bekijk nog eens de list-functies (Perkovic, blz. 28).
# decalre 
list = [1,2,3,4,5,6,7]
getallen = [5,4,5,5]

# methods
def som(lijst_voor_functie): 
	sum_van_list = sum(lijst_voor_functie)
	return sum_van_list
# klaar

def verschil(lijst_voor_functie):
	verschil_functie = lijst_voor_functie
	print("vis")
# klaar

# hoofd programma
print("Som: ", som(list))
