
#Practice Exercise 1_2(strings)
#A: 
aantal_letters = len("Supercalifragilisticexpialidocious")
print("A: Supercalifragilisticexpialidocious heeft " + str(aantal_letters) + " letters \n")


#B: 
print("B: Komt ice voor in 'Supercalifragilisticexpialidocious'")
antwoord_b =  "ice" in "Supercalifragilisticexpialidocious"
print(str(antwoord_b) + ".\n")


#C
print("C: Is het woord 'Antidisestablishmentarianism' langer dan 'Honorificabilitudinitatibus'?")
antwoord_c = 'Antidisestablishmentarianism' > 'Honorificabilitudinitatibus'
print( str(antwoord_c) + ".\n")


#D
componisten_list = ['Berlioz', 'Borodin', 'Brian', 'Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
componisten_list.sort()
print("D: Welke componist komt in alfabetische volgorde het eerst: " + componisten_list[0] + "\n")