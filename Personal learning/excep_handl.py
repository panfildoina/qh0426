
#Asking user for two number

def devide_numbers(): 
    try:
        num1 = float(input("Introduce your first number: "))
        num2 = float(input("Introduce your second number: "))
        result = num1 / num2
        print(f"The result is {result}")
#adding exception in case num 2 value is 0    
    except ZeroDivisionError:
        print("Whoops! You can't devide by zero")
#adding exception in case one of the numbers is any other character then number
    except  ValueError:
        print("Invalid input. Please enter a number")
devide_numbers()

#File reading with finally block program 
def read_file(filename):
    try:
        file = open (filename, 'r')
        content = file.read()
        print(content)
    except FileNotFoundError:
        print(f"The file {filename} was not found")
    finally:
        if 'file' in locals():
            file.close()
            print("The file has been closed.")
#test the function

read_file("D:\CYBER SECURITY\Programming\qh0426\Personal learning\some_file.txt")