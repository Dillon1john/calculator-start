#Calculator
from art import logo


#Add
def add(n1,n2):
    """Adds variables together for calculator device """
    return n1 + n2

#Subtract
def subtract(n1,n2):
    """Subtracts variables for calculator device """
    return n1 - n2

#Multiply
def multiply(n1,n2):
    """Multiplies variables together for calculator device """
    return n1 * n2

#Divide
def divide(n1,n2):
    """Divides variables for calculator device """
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
 #Pulls function from dictionary and assigns it to value called function you can call 
 #as if you were calling the original function
# function = operations["+"]
# function(2,3)
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))


    for symbol in operations:
        print(symbol)
    keep_going = True
    while keep_going:    
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calc_function = operations[operation_symbol]
        answer = calc_function(num1,num2)
    
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input(f" Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:\n")

        if should_continue.lower() == "y":
            keep_going = True
            num1 = answer
        else:
            keep_going = False 
            calculator()   


calculator()