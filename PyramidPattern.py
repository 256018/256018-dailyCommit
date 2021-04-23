def pattern(n):
	# number of spaces
	space = 2*n - 2
	for i in range(0, n):
		for j in range(0, space):
			print(end=" ")
		for k in range(0, i+1):
			print("* ", end="")
		print()
		space = space - 2
n = 5
pattern(n)
