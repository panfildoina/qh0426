#Creating a program that takes the user on a mini adventure.
#Finding out adventure type
print ("What type of advendure should I have?")
adventure_type = input()
if (adventure_type == "scary") or (adventure_type == "short"):
      print("Entering the dark forest!.")
elif (adventure_type == "safe") or (adventure_type == "long"):
     print("Taking the safe route!")
else:
    print("Not sure which route to take.")

#new program that details what happens in the dark forest.
print("What did I hear?")
heard = input()
print("What did I see?")
seen = input()
 # Identify and display

if (heard == "grrr") and (seen == "two red eyes"):
     print("There is a scary creature. I should get out of here!")
else:
     print("I am a little scared but I will continue.")

#2nd way 
user = input("What did I hear? ")
see = input("What did I see? ")

#determine what message to display
if (user == "grr") and (see == "two red eyes"):
     print("There is a scary creature. I should get out of here")
else: 
     print("I am a little scared but I will continue")



