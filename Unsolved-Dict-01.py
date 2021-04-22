def MergeTwoDictionary(dict1, dict2):
	return(dict1.update(dict2))

# First Dictionary 
dict1 = {1: 'MON', 2: 'TUE' , 3: 'WED', 4: 'THUR'}

# Second Dictionary
dict2 = {5: 'FRI', 6: 'SAT', 7: 'SUN'}

# Calling Merge Function
print(MergeTwoDictionary(dict1, dict2))

# Printing Updated first Dictionary
print(dict1)
