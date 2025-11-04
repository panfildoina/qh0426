#We wish to create a program to retrieve some numbers and calculate their sum.
#Asking user how many numbers to sum up
user = int(input("How many numbers should I sum up?\n"))
sum = 1 #sum starts at 1
print()
total = 0 #total starts at 0
while sum <= user:
   print(f"Please enter the number {sum} of {user}:\n")
   number = int(input())
   total = total + number
   sum += 1
print(f"The answer is {total}")

