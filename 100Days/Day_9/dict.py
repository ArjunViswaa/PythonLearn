programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# print(programming_dictionary["Function"])

programming_dictionary["Loop"] = 'The action of doing something over and over again.'
# print(programming_dictionary)

empty_dict = {}
# programming_dictionary = {}

# print(programming_dictionary)

programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)


# for key in programming_dictionary : 
#     print(key)
#     print(programming_dictionary[key])

# Nested List...
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}

# print(travel_log["France"][1])

nested_list = ['A', 'B', ['C', 'D']]
# print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dilon"]
    },
    "Germany": {
        "num_times_visited": 2,
        "cities_visited": ["Stuttgart", "Berlin"]
    }
}