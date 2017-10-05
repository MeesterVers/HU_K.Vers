set1 = set()
set2 = set()
set3 = set()

for i in range(1, 1000):
	if i % 3 == 0:
		set1.add(i)
		# print(set1)

for i2 in range(1, 1000):
	if i2 % 7 == 0:
		set2.add(i2)
		# print(set2)

for i3 in range(1, 1000):
	set3.add(i3)

print("A")
print(set1 & set2)

print('\n')

print("B")
print(set1 | set2)

print('\n')

print("D")
print(set3 - set1 - set2)