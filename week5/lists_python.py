#creating a list of movement steps and returning it.

def directions ():
    steps = []
    steps.append("Move Forward")
    steps.append("Move Backward")
    steps.append("Turn Left")
    steps.append("Turn Right")
    return steps

def run_task1():
    steps_list = directions()
    print(steps_list)

if __name__ == "__main__":
    run_task1()
#creating a list containing directions AND the number of steps
def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Turn Left", 3, "Turn Right", 1]
    return path
# This function prints "Moving...", gets the list from movements(),
# and displays each pair (direction + steps)
def run_task2():
    print("Moving...")
    path = movements()
    
    for i in range(0, len(path), 2):
       directions = path[i]
       steps = path[i + 1]
       print(f"{directions} for {steps} steps")

if __name__ == "__main__":
    run_task2()
#Task 3 
#creating  and returning  a list of directions
def directions():
    steps = []
    steps.append("Move Forward")
    steps.append("Move Backward")
    steps.append("Turn Left")
    steps.append("Turn Right")
    return steps
#Displaying menu of directions with index numbers
def menu():
    print("Please select a direction...")
    steps_list = directions()

    for index in range(len(steps_list)):
        direction = steps_list[index]
        print(f"{index}: {direction}")

#Calling menu function
def run_task3():
    menu()

# Ensures the program runs only when executed directly
if __name__ == "__main__":
    run_task3()