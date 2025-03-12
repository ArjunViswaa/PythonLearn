a = 10
b = 20

# AND Operator : 
print("AND Operation : ")
print(a == 10 and b == 20) # True and True = True
print(a == 10 and b == 30) # True and False = False
print(a == 20 and b == 30) # False and False = False


# OR Operator : 
print("OR Operation : ")
print(a == 10 or b == 20) # True or True = True
print(a == 10 or b == 30) # True or False = True
print(a == 20 or b == 30) # False or False = False

# NOT Operator : 
print("NOT Operation : ")
print(not a == 10) # not True = False
print(not a == 20) # not False = True