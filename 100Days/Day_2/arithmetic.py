print(123 + 456) # Add

print(7 - 3) # Subtract

print(5 * 18) # Multiplication

print(5 / 3) # Division and returns a float

print(5 // 3) # Division and returns an integer

print(5 ** 2) # 5 to the power of 2

# Priority - PEDMAS or BODMAS

print(3 * 3 + 3 / 3 - 3 + 3 ** 3)
# Exponent -> 3 ^ 3 = 27 => 3 * 3 + 3 / 3 - 3 + 27
# Multiplication -> 3 * 3 = 9 => 9 + 3 / 3 - 3 + 27
# Division -> 3 / 3 = 1 => 9 + 1.0 - 3 + 27
# Addition -> 9 + 1.0 = 10.0; 10.0 + 27 = 37.0 => 37.0 - 3
# Subtraction -> 37.0 - 3 = 34.0