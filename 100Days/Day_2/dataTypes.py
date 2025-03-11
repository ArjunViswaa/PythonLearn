# print(len(12345)) # TypeError: object of type 'int' has no len()

# print("Hello"[0]) # Subscripting - prints "H"
# print("Hello"[-1]) # Subscripting reverse - prints "o"

# print("123" + "345", type("123345")) # Prints concatenated value - "123345" since both are strings
# print(123 + 345) # Prints sum - 468

# print(123_456_789, type(123_456_789)) # Represent large numbers by splitting it by _ still an int

# print(12345.456, type(12345.456) ) # float

# print(True, type(True)) # bool
# print(False, type(False)) # bool

# type(obj) - return what the datatype of the given obj is

# Data Type conversion... TypeCasting
# print(int("123") + int("345")) # Prints 123 + 345 = 468

# Task 2
print("Number of letters in your name: " + str(len(input("Enter your name"))))