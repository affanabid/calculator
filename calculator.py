def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
}
def calculator():
    num1 = float(input("Enter First number: "))
    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol, end=' ')
        print()
        operation_symbol = input("What operation do you want to perform? ")
        num2 = float(input("Enter next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'y' if you want to continue with {answer}, or 'n' if you want to start again.") == 'y':
            num1 = answer
        else:
            should_continue = False
        calculator()
calculator()