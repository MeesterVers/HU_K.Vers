week = {'ma': 'maandag', 'di': 'dindag', 'wo': 'woensdag', 'do': 'donderdag', 'vr': 'vrijdag'}

week['za'] = 'zaterdag'
print(week)
print('\n')

for afkorting in week.keys():
	print(afkorting)

print('\n')
for lange_naam in week.values():
	print(lange_naam)

print('\n')
for beide in week.items():
	print(beide)

print('\n')
for afkorting in week.keys():
	# print(afkorting, week[afkorting])
	print('Afkorting: {}, Lange naam: {}' .format(afkorting, week[afkorting]))