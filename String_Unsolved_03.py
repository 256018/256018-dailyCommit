def firstrepeatedChar(str):
	l = {}
	for char in str:
		if char in l:
			return char;
		else:
			l[char] = 0
	return '\0'

print(firstrepeatedChar("PythonForBeginners"))
