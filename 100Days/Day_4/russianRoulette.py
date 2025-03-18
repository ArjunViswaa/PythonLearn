import random

friends = ["Chandler", "Monica", "Ross", "Rachael", "Joey", "Phoebe"]

who_pays_bill = random.choice(friends) # Method 1
print(who_pays_bill)

random_index = random.randint(0, 5) # Method 2
who_pays_bill = friends[random_index]

print(who_pays_bill)