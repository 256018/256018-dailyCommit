from statistics import mean
list1 = [{'abc' : 34, 'def' : 8, 'ghi' : 10},
			{'xyz' : 1, 'pqr' : 10, 'lmn' : 9, 'stu' : 5, 'hij' : 12},
			{'ska' : 8, 'pen' : 3, 'axv' : 3, 'ert' : 8}]
			

print("Original list: " + str(list1))

res = dict()
for sub in list1:
	for key, val in sub.items():
		if key in res:
			res[key].append(val)
		else:
			res[key] = [val]

for key, num_l in res.items():
	res[key] = mean(num_l)

print("Average is : " + str(res))
