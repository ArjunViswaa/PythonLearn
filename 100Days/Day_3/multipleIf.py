height = int(input("What is your height ? "))

if height > 180 : 
    print("You can ride the roller coaster")
    age = int(input("What's your age ? "))
    if age < 12 : 
        bill = 5
        print("Children ticket price is 5$.")
    elif age <= 18 : 
        bill = 7
        print("Teenagers ticket price is 7$.")
    else : 
        bill = 12
        print("Adults ticket price is 12$.")

    wantPhoto = input("Do you want a photo ? Type y for yes and n for no ")
    if wantPhoto == "y" : 
        bill += 3
    
    print(f"Your final bill is {bill}$")

else : 
    print("Sorry you're not allowed to ride the roller coaster..")