import xmltodict

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
