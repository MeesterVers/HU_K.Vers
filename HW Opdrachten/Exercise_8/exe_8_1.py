bruin = set(["Boxtel", "Breukenlaan", "Eindhoven", "Helmond 't Hout", "Helmond", "Helmond Brouwhuis", "Deurne"])
groen = set(["Boxtel", "Breukenlaan", "Eindhoven", "Geldrop", "Heeze", "Weert"])

print("\nOvereenkomst:")
print(bruin.intersection(groen))
print("\n")

print("Verschil bruin groen:")
print(bruin.difference(groen))
print("\n")

print("Alle stations:")
print(bruin.union(groen))