#Writing a program to classify books 
#Asking  user to enter cover type
print("What is the cover type of the book (hard/soft)?")
cover_type = input()
#decide if cover book is soft or hard
if cover_type == "soft":
    #ask user if the books is perfect bound
    print("Is the book perfect-bound?")
    answer=input()
    if answer == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else: 
        print ("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")

#New
#Ask user where should he look

print("Where should I look?")
location = input()
#If location in the bedroom
if location == "in the bedroom":
    print("Where in the bedroom should I look?")
    answer=input()
    if answer == "under the bed":
         print("Found some shoes but no phone.")
    else: 
         print("Found some mess but no phone.")

#if location in the bathroom
if location == "in the bathroom":
    print("Where in the bathroom should I look?")
    answer=input()
    if answer == "in the bathtub":
         print("Found a rubber duck but no phone")
    else: 
         print("Found bathroom stuff but no phone.")
    
#if location in the living room
if location == "in the living room":
    print("Where in the living room should I look?")
    answer=input()
    if answer == "on the table":
         print("Yes! I found my phone!")
    else: 
         print("Found some stuff but no phone.")

else:
    print("I do not know where that is but I will keep looking.")
         
         
