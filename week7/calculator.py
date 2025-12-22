def add(a, b):
    return a +b 
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a * b
def division(a, b):
    return a / b 

while True: 

    try:
        num1 = float(input("Enter the first number: "))
        operation = input("Choose an operation (+, - , *, /): ")
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Enter a valid number")
        continue
    try:
        if operation == "+":
            result = add(num1, num2)
            break
        elif operation == "-":
            result = subtract(num1, num2)
            break
        elif operation == "*":
            result = multiply(num1, num2)
            break
        elif operation == "/":
            try:
                result = division(num1, num2)
                break
            except ZeroDivisionError:
                print("Error: Division by zero is not possible")
                continue
        else: 
            print("Invalid operation, try again")
            continue
print("Result:", result)

    except:
        print("Unknown error, try again")
    
    start_again = input(" Do you want to calculate again? yes/no ").lower()
    if start_again != "yes":
        print("Thank you for using the calculator")
        break





    
