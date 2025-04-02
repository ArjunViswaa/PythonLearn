import art

def add(n1, n2) : 
    return n1 + n2

def subtract(n1, n2) : 
    return n1 - n2

def multiply(n1, n2) : 
    return n1 * n2

def divide(n1, n2) : 
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator() : 
    print(art.logo)
    first_number = float(input("What is the first number : "))
    should_continue = True
    while should_continue : 
        for symbol in operations : 
            print(symbol)
        math_op = (input("Pick an operation : "))

        next_number = float(input("What is the next number : "))

        answer = operations[math_op](first_number, next_number)
        print(f"{first_number} {math_op} {next_number} = {answer}")
        continutation = input(f"Do you wish to continue with this output {answer} ? Select 'y' for Yes or 'n' for No : ")
        if continutation == "y" : 
            first_number = answer
        else : 
            print("\nThanks & Bye !!!")
            should_continue = False
            calculator()

calculator()