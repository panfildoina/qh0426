#Asking user how far are from the target
steps = int(input("How far are we from the target?\n"))

print()

#Use a for loop to count down
for i in range(steps, 0, -1):
    
    print(f"{i} steps remaining")
print()
print("Target achieved!")