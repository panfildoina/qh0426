#Defining guess number
guess_number = 16

#Initialize user guess to none
user_guess = None

while user_guess != guess_number:
    #get user's guess
    user_guess = int(input("Guess the number: "))

    if user_guess < guess_number:
        print("The number is too low! Try again.")
    elif user_guess > guess_number:
        print("The number is too high. Try again!")
    else:
        print("Congratulations! The number is correct!")