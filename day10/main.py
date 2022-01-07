from art import logo 
print(logo)

#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

def calculator():
    operations = {
        "+" : add,
        "-" : substract,
        "*" : multiply,
        "/" : divide
    }
    num1 = float(input("What's the first number?: "))
    for i in operations:
        print(i)
    repeat_cond = True
    while repeat_cond == True:    
        operation_symbol = input("Pick an operator: ")
        num2 = float(input("What's the next number?: "))
        cal_function = operations[operation_symbol]
        answer1 = cal_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer1}")
        repeat = input(f"Type 'y' to continue with {answer1} type 'n' to exit: ") 
        if repeat == "y":
            num1 = answer1
        else:
            repeat_cond = False
            calculator()

calculator()