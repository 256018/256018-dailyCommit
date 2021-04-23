def pattern(n):
	# number of spaces
	spaces = n - 1
	for i in range(0, n):
		for j in range(0, spaces):
			print(end=" ")
		spaces = spaces - 1
		for j in range(0, i+1):
			# printing stars
			print("* ", end="")
		print()
# Driver Code
n = 7
pattern(n)
