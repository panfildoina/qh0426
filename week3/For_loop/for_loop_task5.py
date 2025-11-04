user = input("What word do you see?\n ")

print("\nDisplaying index positions...\n")

for count in range(0, len(user), 1):
    print(f"index: {count}", user[count])