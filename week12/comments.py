"""
Stage changes by adding new or modified files to the staging area → git add

Check the state of the local repository → git status

Save the changes to the local repository → git commit

Update the local repository with content from the remote → git pull

Upload the local repository content to the remote → git push

"""

"""
Elderly OR with children	(age > 55) or (with_children == True)
Disability priority	with_disability == True
Elderly + disability combined	(age > 55) or (with_disability == True)


toys.union({...})	{car, robot, doll, marble, fidget spinner}
toys.union(toys)	{car, robot, doll}
toys.append("marble")	TypeError / Error

"""

"""
Automatically closes file	with open("salaries.txt") as f:
Opens file in write mode	open("salaries.txt", "w")
Keyword to create alias	as
Opens file in read mode	open("salaries.txt", "r")


"""
"""
letters = ["a", "b", "c"]  #list
print(example[0])   #tupple 
example[0] = "new value"
#values inside a tuple are ordered 
# a set cannot contain duplicate values
#values inside set a unordered 
for key,value in data.items()   #dictionary
"""

"""
Loop through the tuple → for drink in drinks:
Second drink → drinks[1]
Total number → len(drinks)
Create tuple → drinks = ("Coffee", "Tea", "Juice")

"""

"""
Creates a list with no items wish_list = []

Displays the list  print(wish_list)

asks user if they wan to add another item
choice = input("Would you like to add an item to your wish list? (y/n)")

loops through the list for item in wish_list

asks the user to enter an item and store it in the list
wish_list.append(input("Enter an item to add to your wish list: "))

"""
"""
Display percentace > pie chart
Display hierachical view > tree map
display the frequency calling a helpline > bar chart
Display the relationship between two variables > scatter plot
Display the real time change in stock prices > line plot
"""


"""
Import + alias	> from utils import update_details_and_export_to_file as update_export
Import function	from utils > import update_details_and_export_to_file
Import one specific function	> from utils import read_from_file
Import all	> from utils import *
"""

"""
Retrieve the total number of suits in the tuple > len(suits)
Retrieve the first suit from the tuple > suits[0]
Retrieve the fourth suit in the tuple >  suits[3]
Create a tuple pre-populated with the name of each suit  > ("Hearts", "Diamonds", "Clubs", "Spades")
"""
"""
drinks_tuple = ("tea", "coffee", "water")  # Creates a tuple containing the names of drinks
for drink in drinks: # Loops through each drink in the tuple
 drinks[1]  # Retrieves the second drink (index 1) from the tuple
 print(len(drinks)) # Displays the total number of drinks in the tuple
"""
"""
Prioritise children > 	age < 18
Elderly + medical history > 	age > 55 and history_of_medical_conditions == True
Children/elderly + medical history > 	(age < 18 or age > 55) and history_of_medical_conditions == True
Children or elderly > 	age < 18 or age > 55
Medical history	> history_of_medical_conditions == True

"""

"""
Creates an empty list that can be used to store the names of each item. → items = [],

Iterates through each item in the shopping list → for item in items:,

Displays an item from the shopping list → print(item),

Adds the name of each item entered by the user to the shopping list. → items.append(input()),

Reads in the number of items to be stored in the shopping list. → n_items = int(input())

"""