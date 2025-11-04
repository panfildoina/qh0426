print("Program started...")

user = input("Please enter standard character:\n")

if len(user) ==1:
    print(f"The ASCII code for {user} is {ord(user)}")
else:
    print("A single characted was expected...")

print("Program Ended!")