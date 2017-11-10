import xmltodict
synomiemenlijst = []

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

stationsdict = processXML('FA10.xml')
stations = stationsdict['Stations']['Station']

print('\nDit zijn de codes en types van de 4 stations:')
for station in stations:
	print('{:4} - {}'.format(station['Code'], station['Type']))
	
print('\nDit zijn alls stations met een of meer synomiemen:')
for station in stations:
	try:
		print("{:4} - {}" .format(station['Code'], station['Synoniemen']['Synoniem']))
	except TypeError:
		pass

print('\nDit is de lange naam elk station:')
for station in stations:
	print("{:4} - {}" .format(station['Code'], station['Namen']['Lang']))