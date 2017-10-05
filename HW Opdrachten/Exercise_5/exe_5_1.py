def convert(temperatuur_celsius):
	temperatuur_fahrenheit = temperatuur_celsius * 1.8 + 32
	return temperatuur_fahrenheit

def table(start_range, end_range):
	for waarde in range(start_range, end_range, 10):
		converted_waarde = convert(waarde)
		print("{} {}" .format(converted_waarde, waarde))


temperatuur_celsius_start = eval(input('Vul de start temperatuur in grade celsius in: '))
temperatuur_celsius_end = eval(input('Vul de eind temperatuur in grade celsius in: '))

antwoord = table(temperatuur_celsius_start, temperatuur_celsius_end)