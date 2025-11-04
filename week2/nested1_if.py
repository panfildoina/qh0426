#Ask User where should he look
print("Where should I look? ")
location = input ()
if location == "in the bedroom":
    print("Where in the bedroom should I look? ")
    location_1=input
    if location_1 == "under the bed":
        print("Found some shoes but no phone?")
    else:
        print("Found some mess but no phone.")

if location == "in the bathroom":
    print("Where in the bathroom should I look? ")
    location_1=input
    if location_1 == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")

if location == "in the living room":
    print("Where in the living room should I look? ")
    location_3=input
    if location_3 == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")
else:
    print("I do not know where that is but I will keep looking.")

    