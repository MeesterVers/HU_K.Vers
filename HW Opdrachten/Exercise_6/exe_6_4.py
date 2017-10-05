studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
	som_student = 0
	gemiddelde = 0
	aantal_cijfers_per_student = 0
	lijst_som_cijfers = []

	for studentcijfers in studentencijfers:
		aantal_cijfers_per_student = len(studentcijfers)
		for cijfer in studentcijfers:
			som_student = cijfer + som_student
		gemiddelde = som_student // aantal_cijfers_per_student
		lijst_som_cijfers.append(gemiddelde)
		som_student = 0
		gemiddelde = 0
	antw = lijst_som_cijfers
	return antw

def gemiddelde_van_alle_studenten(studentencijfers):
	gemiddelde = 0
	som_studenten = 0
	aantal_cijfers = 0

	for studentcijfers in studentencijfers:
		aantal_cijfers = len(studentcijfers) + aantal_cijfers
		for cijfer in studentcijfers:
			som_studenten = cijfer + som_studenten
		antw = som_studenten // aantal_cijfers
	return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))