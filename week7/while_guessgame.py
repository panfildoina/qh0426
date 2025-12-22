import random
def guess_game():
    secret_number = random.randint(1, 10)
    max_attemps = 3 
    attemps = 0
    while attemps < max_attemps:
        try:
            user_guess = int(input("Enter a number between 1 and 10: "))
        except ValueError:
            print("Enter a whole number")
            continue #doesn't count the attempt, goes back to while loop
    #increasing attemps
        attemps += 1
    #checking first attempt
        if user_guess == secret_number:
            print(f"You guessed the correct number. Congratulations, number {secret_number} is the correct one!")
            break 
        elif user_guess > secret_number:
            print("The number is too high, try a lower number: ")
        else:
            print("The number is too low. Try a higher number: ")
    if attemps == max_attemps and user_guess != secret_number:
        print(f"Game over! All {max_attemps} attemps has been used. The number was {secret_number}")

#relaunching the game 
while True:
    guess_game()
    start_new_game = input("Do you want to start again? (yes/no): ").lower()

    if start_new_game != "yes":
        print("Thanks for playing!Bye")
        break

    