# Python3 program to show that the variables with a value
# assigned in the class declaration, are class variables and
# variables inside methods and constructors are instance
# variables.
class Dog:
	# Class Variable
	animal = 'dog'			
	# Constructor
	def __init__(self, breed, color):
	
		# Instance Variable	
		self.breed = breed
		self.color = color	
	
# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)


print("\nAccessing class variable using class name")
print(Dog.animal)	
