def problem() : 
    year = int(input("What's your year of birth?"))

    if year > 1980 and year < 1994:
        print("You are a millennial.")
    elif year > 1994:
        print("You are a Gen Z.")

def solution() : 
    year = int(input("What's your year of birth?"))

    if year > 1980 and year < 1994:
        print("You are a millennial.")
    elif year >= 1994: # Here we include 1994...
        print("You are a Gen Z.")