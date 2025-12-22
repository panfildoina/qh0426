# first create a menu asking for number and operators


print("Welcome to the Calculator")
while True:
    while True: 
        try:
            number_1 =float(input("Enter the first number : "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
    operator = input("Please enter an operator(+, -, *, /) : ")

    while True:
        try: 
            number_2 = float(input("Enter the second number :  "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
        
    print("You have entered: {} {} {}". format(number_1, operator, number_2))
    

    while True:
        if operator == "+":
            result = number_1 + number_2
            break
        elif operator == "-":
            result = number_1 - number_2
            break
        elif operator == "*":
            result = number_1 * number_2
            break
        elif operator == "/":
            if number_2 != 0:
                result =  number_1 / number_2
                break
            else:
                print("Error: Dvision by zero is not allowed.\n")
                operator = input("Please enter a valid operator(+, -, *, /) : ")
                number_2 = float(input("Enter the second number : "))
        else: 
            print("Invalid operator. Please try again.\n")
            operator = input("Please enter a valid operator(+, -, *, /) : ")
            number_2 = float(input("Enter the second number : "))
        
    print("The result of {} {} {} = {} ". format (number_1, operator, number_2, result))
    # ask the user if they want to perform another calculation
    choice = input("Do you want to perform another calculation? (yes/no): ")
    if choice.lower() != "yes":
        break
    
    print("Thank you for using the calculator. Goodbye!")