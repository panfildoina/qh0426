#exercise 1:
try:
    num1 = float(input("Enter the first number:" ))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} devided by {num2} is {result}")
except ZeroDivisionError:
    print("Sorry, you can't devide by zero!")
except ValueError:
    print("Oops! That's not a valid number")
#exercise 2:

try:
    with open('nonexistent_file.txt', 'r') as file:
        print(file.read())
except FileNotFoundError:
    print("Oops, file not found")

#exercise 3:
my_list = [2,"3", 0, "apple", 4]

try:
    for item in my_list:
        try:
            print(int(item))
        except ValueError:
            print(f"Can't convert {item} to an integer.")
except Exception as e:
    print(f"An unexpected error occured: {e}")
finally:
    print("Loop completed.")
