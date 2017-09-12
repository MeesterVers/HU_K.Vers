#Practice Exercise 2_2 (getallen, strings en conversie)
cijferICOR = 8
cijferPROG = 10
cijferCSN = 10
cijfers = [cijferICOR, cijferPROG, cijferCSN]
beloning_per_cijfer = 30

gemiddelde = sum(cijfers) / len(cijfers)
beloning = sum(cijfers) * beloning_per_cijfer
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van € ' + str(beloning) + ' op!'

print(overzicht)