#1
def displaySmallest(num1, num2):
  if num1 < num2:
      return num1
  return num2

displaySmallest (7, 5)

#Select the missing word in the following cases:

#[num2] is a parameter for the function.

#[num1 < num2] is a condition.

#[displaySmallest] is the function name
#[7] is an argument.

#[displaySmallest (7, 5)] is a function call.

#[return] is a keyword that is used to respond to a function call with a value.#

#2 
print ("Please entrt your name")
name = input()
print (f"Hello {name}")

#3
for count in range (20, 31, 2):
    print(count)
  #print numbers from 20 to 30 with step of 2

#4
even_total = 0              # Initialise the total for even numbers
odd_total = 0               # Initialise the total for odd numbers

for count in range(5):      # Loop to read 5 numbers from the user
    print("Please enter a whole number")   # Prompt the user for input
    user_number = int(input())             # Read and convert input to an integer

    if user_number % 2 == 0:                # Check if the number is even
        even_total += user_number           # Add the number to the even total
    else:                                   # Otherwise, the number is odd
        odd_total += user_number            # Add the number to the odd total

print(f"The total of even numbers is {even_total}.")  # Display total of even numbers
print(f"The total of odd numbers is {odd_total}.")    # Display total of odd numbers


#5

if user_number in numbers_list:
    print("The number is in the list")
else:
    print("The number is not in the list")



#6
def bill_data():
    data = {"age": 29, "favourite colour": "blue"}
    return data


def viola_data():
    data = {"age": 27, "favourite colour": "violet"}
    return data


def rizzy_data():
    data = {"age": 31, "favourite colour": "red"}
    return data


def assemble():
    return {
        "bill": bill_data(),
        "viola": viola_data(),
        "rizzy": rizzy_data()
    }


def display():
    for key, value in assemble().items():
        print(f"{key}: {value}")


display()


#7 

time_gained = 0                     # Initialise total time gained/lost to zero

for count in range(6):              # Loop to read times for 6 people
    print("Please enter a time in minutes:")   # Prompt the user for input
    time_taken = int(input())       # Read and convert the input to an integer

    if time_taken > 90:             # Check if the task was completed late
        time_gained -= time_taken - 90   # Subtract extra minutes lost
    else:                           # Otherwise, the task was on time or early
        time_gained += 90 - time_taken   # Add minutes saved

print(f"{time_gained} minutes were gained")    # Display the total time gained

# def buy_drink(weather, money):            # Define the function with weather and money as parameters

    if weather == "cold" and money >= 3.15:   # Check if it is cold and enough money for coffee
        print("Coffee")                       # Display Coffee

    elif weather == "warm" and money >= 3.35: # Check if it is warm and enough money for iced tea
        print("Iced tea")                     # Display Iced tea

    else:                                    # Any other combination of weather and money
        print("Water")                       # Display Water


buy_drink("warm", 10.55)                     # Call the function with sample values


#8
def yes_no_question(check):
    # Ask the user a yes/no question based on the check value
    response = input(f"Is it {check}? (y/n)")

    # Check if the response is 'y' (case-insensitive)
    if response.lower() == "y":
        return True            # Return True if the answer is yes
    return False               # Return False for any other answer


def drying_speed(is_sunny, is_windy):
    # Determine drying speed based on weather conditions
    if is_sunny and is_windy:
        return "Fast"          # Clothes dry fast if it is sunny and windy
    elif is_sunny or is_windy:
        return "Slow"          # Clothes dry slowly if only one condition is true
    return "not drying"        # Clothes do not dry if neither condition is true


def dry_clothes():
    # Ask the user if it is sunny
    sunny = yes_no_question("sunny")

    # Ask the user if it is windy
    windy = yes_no_question("windy")

    # Calculate the drying speed based on the conditions
    speed = drying_speed(sunny, windy)

    # Display the drying status
    print(f"The drying status of your clothes is: {speed}")


if __name__ == "__main__":
    # Run the dry_clothes function when the program starts
    dry_clothes()

#9

def explain(what, where):
    # Check if the monster is under the bed
    if what == "Monster" and where == "Bed":
        print("I'm friends with the monster that's under my bed.")

    # Check if the doctor is in the head
    elif what == "Doctor" and where == "Head":
        print("You're trying to save me, stop holding your breath.")

    # Handle all other combinations
    else:
        print("You think I'm crazy, yeah, you think I'm crazy.")


# Call the function with sample arguments
explain("Monster", "Bed")

