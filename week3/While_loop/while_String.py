#Creating a program with while loop with len function
#len() built-in function -returns # of items in an object

#Asking user input
user = input("Please enter a phrase:\n")
print()
phrase = 0

#The program should then display the word "Hi" repeatedly x number of times where x is the number of characters in
#the phrase entered by the user.

while phrase < len(user):
    print("Hi ", end="")
    phrase +=1
