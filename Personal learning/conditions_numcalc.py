num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operator = input("Enter an operator(+, -, *, /): ")

if operator == "+":
    print(f"The result is: {num1 + num2}")
    
elif operator == "-":
    print(f"The result is: {num1 - num2}")
elif operator == "*":
    print(f"The result is: {num1 * num2}")
elif operator == "/":
    if num2 != 0: 
        print(f"The result is: {round(num1 / num2, 2)}")
    else:
        print("Cannot devide by 0")
else:
    print("Invalid operator")
