height = int(input("What is your height ? "))

if height > 180 : 
    print("You can ride the roller coaster")
    age = int(input("What's your age ? "))
    if age < 12 : 
        print("Please pay 5$.")
    elif age <= 18 : 
        print("Please pay 7$.")
    else : 
        print("Please pay 12$.")

else : 
    print("Sorry you're not allowed to ride the roller coaster..")