#create a program that allows a robot to avoid obstacles.
#Asking for user input

user = int(input("How many obtacles must I avoid? "))
obstacles_avoided = 0
print()

while obstacles_avoided < user:
    print("Avoiding...", end="") #stay on the same line
    obstacles_avoided +=1
    print(f"Done! {obstacles_avoided} obstacles avoided.")

print("All obstacles have been avoided")


    













