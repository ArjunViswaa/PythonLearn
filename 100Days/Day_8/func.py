def greet(name, timeOfDay) : 
    print(f"Hello {name}")
    print(f"How are you this {timeOfDay} ? ")

# greet("Arjun", "evening")

def life_in_weeks(age) : 
    age_left = 90 - age
    age_left_in_weeks = age_left * 52
    print(f"You have {age_left_in_weeks} weeks left.")

# life_in_weeks(56)

# Keyword arguments instead of positional arguments
def greetKey(name, timeOfDay) : 
    print(f"Hello {name}")
    print(f"How are you this {timeOfDay} ? ")

greetKey(timeOfDay="morning", name="Arjun")