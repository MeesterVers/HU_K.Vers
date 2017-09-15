def new_password(oldpassword, newpassword):
	if oldpassword != newpassword and len(newpassword) >= 6:
		for c in newpassword:
			if c in '0123456789':
				return True
		return False
	else:
		return False

# Correct wachtwooorden --> True
output0 = new_password('vakProg17', 'python17')
print(output0)

# Incorrect wachtwooorden --> False
output1 = new_password('vakProg17', 'vakProg17')
print(output1)

# Incorrect wachtwooorden --> False
output2 = new_password('vakProg17', 'Pro17')
print(output2)

# Incorrect wachtwooorden --> False
output3 = new_password('vakProg17', 'python')
print(output3)