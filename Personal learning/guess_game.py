import random

secret_number = random.randint(6, 16)
guess_number = int(input("Guess a number betweeen 1 and 10: "))
if guess_number == secret_number:
    print(f"You have guessed the number! The number was indeed {secret_number}")
elif guess_number < secret_number:
    print(f"The number was not {guess_number}, please try again!\n")))
         if guess_number == secret_number:
              print("You guessed it on the second try!")

else:
    print(f"Well, the number was not {guess_number}, actually it was {secret_number}")