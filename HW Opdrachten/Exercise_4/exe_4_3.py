def lang_genoeg(lengte):
	if lengte >= 120:
		return print('Je bent lang genoeg voor de attractie!')
	else:
		return print('Sorry, je bent te klein!')

gebruiker_lengte = eval(input('Wat is uw lengte? '))
lang_genoeg(gebruiker_lengte)