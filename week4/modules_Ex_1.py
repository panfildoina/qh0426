import random

min_value = int(input("Please enter the minimum value: "))

max_value = int(input("Please eter the maximum value: "))

random_number = random.randrange(min_value, max_value)

print(f"""I am thinking of a number between
      {min_value} and {max_value}.
      Can you guess what it is?""")

print("Can you guess the number? ")

guessed_correctly = False

while not guessed_correctly:
    guess = int(input("Please enter a number: "))

    if guess == random_number:
        print("You guessed correctly")
        guessed_correctly = True
    elif guess < random_number:
        print("Guess number is higher")
    else:
        print("Guess number is lower")
        
print("Game over...")