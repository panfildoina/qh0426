#Creating a program that stimulates lightining 
user = int(input("What level of brightness is required?\n"))

print()

print("Adjusting brightness...\n")

for brightness in range (2, user +1, 2):
    print(f"Brightness level:{'*' * brightness}")

print ("Complete")
