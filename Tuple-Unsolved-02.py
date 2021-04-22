# Using dict() Method
tuple1 = [("Mon", 1), ("Tue", 2), ("Wed", 3),("Thu", 4), ("Fri", 5),]
dictionary = {}
dictionary = dict(tuple1)
print(dictionary)


# Using setdefault() method
tuple1 = [("Mon", 1), ("Tue", 2), ("Wed", 3),("Thu", 4), ("Fri", 5),]
dictionary = {}
for a, b in tuple1:
	dictionary.setdefault(a, []).append(b)
print(dictionary)
