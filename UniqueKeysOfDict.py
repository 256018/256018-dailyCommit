from itertools import chain
def UniqueKeys(arr):
	res = list(set(val for dic in arr for val in dic.keys()))
	# Print the list of unique keys
	print(str(res))
arr = [{'Delhi': 1, 'Mumbai': 2},
	{'Delhi': 1, 'Noida': 3},
	{'Mumbai': 2}]

UniqueKeys(arr)
