num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
math_operator = input("Enter an operator: ")

if math_operator == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif math_operator == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif math_operator == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif math_operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose an option +, -, *, or /.")
