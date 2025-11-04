#Create a program about books
print("What type of book is this?")
book = input()
if book == "adventure":
    print("I like adventure books!")

print("Finished reading book")

#Create a program for activity

print("Please enter the activity to be performed.")
activity = input()
if activity == "calculate":
    print ("Performing calculations...")
else:
    print("Activity completed")

#Program for robot directions
direction = input("Towards which direction I should go (up, down, left or right?)")

if direction == "up":
    print("I am moving in an upward direction!")
elif direction == "down":
    print("I am moving in a downward direction")
elif direction == "left":
    print("I am moving in a left direction")
elif direction == "right":
    print("I am moving in a right direction")
elif direction == "none":
    print ("Your are blocked")
else: 
    print ("I am lost!")
    
#Moludus operator operations
#Ask the user to enter a whole number
num = int(input("Please enter a whole number: "))

#Check if number is even or odd 
if num % 2 == 0:
    print(f"The number {num} is an even number.")
else:
    print (f"The number {num} is and odd number.")

#Comparision operators 
#Asking user to enter first number
num1 = int(input("Please enter the first number: "))
#Asking user to enter second number
num2 = int(input("Please enter the second number: "))
if num1 < num2:
    print(f"The first number is the smallest")
if num1 > num2:
    print(f"The second number is the smallest")
else:
    print(f"Both are equal")

#create a program to count up the number of even and odd numbers.
#Ask the user to enter three whole numbers
num1=int(input("Please enter the first whole number: "))
num2=int(input("Please enter the second whole number: "))
num3=int(input("Please enter the third whole number: "))
#Counting even and odds
even_num = 0
odd_num = 0

#Check first number
if num1 % 2 == 0:
    even_num += 1 #same as even_num = even_count +1
else:
    odd_num += 1
#Check second number
if num2 % 2 == 0:
    even_num += 1 #same as even_num = even_count +1
else:
    odd_num += 1
#Check third number
if num3 % 2 == 0:
    even_num += 1 #same as even_num = even_count +1
else:
    odd_num += 1
#Showing the number of odd and even numbers
print(f"There were {even_num} even and {odd_num} odd numbers.")

