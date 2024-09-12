def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def devide(n1, n2):
    return n1 / n2

# TODO: add functions to a dictionary
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": devide,
}

num1 = float(input("Input the first number: "))
for sym in operations:
    print(sym)
    
operation_sym = input("Pick an operation: ")
num2 = float(input("Input the next number: "))

# TODO: Perform the operation
if operation_sym in operations:
    function = operations[operation_sym]
    result = function(num1, num2)
    print(f"{num1} {operation_sym} {num2} = {result}")
else:
    print("Invalid operation symbol")
