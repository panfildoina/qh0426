#Ask user to enter their name 
print("What is your name?")
name = input()
print(f"It is nice you meet you {name}")

# Display a box
print("##########")
print("#  #  #  #")
print("#        #")
print("##########")

#Ask the user to enter a character for eye

print(f"Please enter a character for the eye")
eye = input()
#Display the robot face using entered character 
print("The robot's expression is now as follows:")

print("##########")
print(f"#  {eye}   {eye} #")
print("#   ---  #")
print("##########")

#New program for calculating bmi 
#Ask the user to enter their name
print("What is your name?")
name = input()

#Ask the user you enter the age
print("What is your age (in years)?")
age = input()

#Ask user to enter their height
print("How tall are you (in meters)?")
height = float(input())

#Ask user what is their weight
print("How much do you weigh (in kilograms)?")
weight = float(input())

#Calculating bmi
bmi =  weight / (height **2)
#Display the result 
print(f"{name} you are {age} years old and your BMI is {bmi:.2f}. ")

#Determine health category
if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category ="normal weight"
elif bmi < 30:
    category = "overweight"
else:
    category = "obese"
print(f"{name} you are {age} years old and your BMI is {bmi:.2f}, which means you are {category} ")


#Ask user to enter their character' stats
print(f"Please enter the number of lives")
lives = int(input())

print(f"Please enter the energy level")
energy = int(input())

print(f"Please enter the shield level")
shield = int(input())

#Display confirmation message 
print ("Health has been set")

#Display using visuals 
print(f"Lives: {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")