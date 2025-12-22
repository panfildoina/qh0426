import random

secret_number = random.randint(2, 20)
maximum_attemps = 3

for attemps in range(maximum_attemps):
    guess_number = int(input("Guess a number between 2 and 20: "))
    if guess_number == secret_number:
         print(f"Correct! The number is {secret_number}")
         break

    elif guess_number > secret_number:
         print("The number is too high! Try a lower number: ")
    
    else:
         print("The number is too low! Try a higher number: ")

else:
     print(f"Game over: All {maximum_attemps} has been used. The number was {secret_number}")

      