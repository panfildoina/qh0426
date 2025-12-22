is_vegetarian = input("Are you a vegetarian? (yes/no): ").lower()

if is_vegetarian == "yes":
    eats_eggs = input("Do you it eggs? (yes/no): ").lower()
    if eats_eggs == "yes":
        print("You can have a veggie omlette")
    else: 
        print("You can have a stir-fry.")
else:
    print("You can have a steak")
print("Bon appetite!")
    
    