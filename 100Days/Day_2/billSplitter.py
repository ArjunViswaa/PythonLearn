print("Welcome to the Bill Splitter application")

bill_amount = float(input("What is the total Bill amount ? $"))
tip_percentage = int(input("What percentage of the bill amount would you like to tip ? 10 12 15"))
total_friends = int(input("How many people to split this bill ? "))

total_amount_to_split = bill_amount * (1 + tip_percentage / 100)
one_share = round(total_amount_to_split / total_friends, 2)

print(f"Each person has to pay $ {one_share} /-")