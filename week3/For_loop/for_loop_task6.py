user = input("What word do you see? in reverse\n ")

print("\nReversing...\n")
print("The phase is ", end="")

for count in range(len(user) -1, -1, -1):
    print(user[count], end="")