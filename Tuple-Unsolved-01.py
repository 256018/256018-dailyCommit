tuple1 = [(1, 2), (3, 4), (10, 9),(1, 2), (11, 5), (3, 4), (10, 9)]
duplicate = False
# To append Duplicate elements in list
l1 = []
count = 0
for i in tuple1:
	# Checking for Duplicates
	if i in l1:
		duplicate = True
		continue
	else:
		count = 0
		for b in tuple1:
			if b[0] == i[0] and b[1] == i[1]:
				count = count + 1
		if(count > 1):
			print(i, "-", count)
		l1.append(i)
