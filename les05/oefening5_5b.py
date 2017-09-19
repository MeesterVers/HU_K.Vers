infile = open('Voorbeeld5_5.txt', 'r')
inhoud = infile.read()
infile.close()

inhoud_lijst = inhoud.split()
print(inhoud_lijst)