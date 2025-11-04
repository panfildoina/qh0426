#Asking User input

name = input("Insert you name: ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("name can be maximum of 50 characters")
else:
    print("name looks good!")