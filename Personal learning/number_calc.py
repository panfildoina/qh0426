#writing a program to do arithmetical operation for addtion
num1 = float(input("Enter your first number for addition: "))
num2 = float(input("Enter your second number for addition:"))
sum_result = num1 + num2
print(f"sum: {num1} + {num2} = {sum_result}")

#writing a program to do arithmetical operation for division
num3 = float(input("Enter your dividend for divion: "))
num4 = float(input("Enter your divisor for division: "))
if num4 == 0:
    print("Error: Division by 0 not possible")
else:
    division_result = num3 / num4
    print(f"Divion result:  {num3} / {num4} = {division_result}")

