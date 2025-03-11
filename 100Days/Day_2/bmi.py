weight = 84
height = 1.65

bmi = weight / height ** 2

print(bmi) # Returns float value due to division involved

print(int(bmi)) # Floors the float value.

print(round(bmi)) # Rounds the floor value as just integer.
print(round(bmi, 2)) # Rounds the floor value to 2 digits.