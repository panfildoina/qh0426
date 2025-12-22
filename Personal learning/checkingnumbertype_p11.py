#checking if number is positive, negative  or zero
num = float(input("Enter a number: "))
if num > 0:
    print(f"The number {num} is a positive number")
elif num == 0:
    print(f"The number {num} is zero")
else:
    print(f"The number {num} is a negative number")