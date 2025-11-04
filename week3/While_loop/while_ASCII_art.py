#creating a  program that simulates a robot charging it's battery.
user = int(input("How many bars should be charged? "))

#Start with 0 bars charge
bars_charged = 0
print()

#While loop to simulate charging 
while bars_charged < user:
    bars_charged +=1
    print(f"Charging: {"█ " * bars_charged}")
    

print("The battery is fully charged.")






















