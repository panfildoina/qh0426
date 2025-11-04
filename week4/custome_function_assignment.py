def escape_by(plan):
    if plan == "A":
        print("We cannot escape that way! The boulder is too big")
    elif plan == "B":
        print("We cannot escape that way! The bouler is moving too fast!")
    elif plan == "C":
        print ("The might work! Let's go!")
    else:
        print("No any other plans...")
    
print("[A] jumping over")
print("[B] running around")
print("[C] cross bridge ahead")
print("[D] other")

user = input("Please enter above phrase:\n")

escape_by(user)