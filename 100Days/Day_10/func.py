def my_function() : 
    result = 3 * 2
    return result

output = (my_function())
# print(output)

def format_name(fName, lName) : 
    formatted_fName = fName.title()
    formatted_lName = lName.title()
    return f"{formatted_fName} {formatted_lName}"

print(format_name("arjun", "viswaa"))