while True:
    print("Please choose one of the following options: \n1-Nice message\n2-Area of a triangle\n3-Times Table\n4-Exit")
    opt = int(input())
    if opt == 1:
        print("You do not smell so bad today!")
    elif opt == 2:
        h = float(input("Enter height: "))
        b = float(input("Enter base: "))
        print(f"The area is {h*b*0.5}cm^2")
    elif opt == 3:
        n = int(input("Enter whole number: "))
        for i in range (1, 11):
        print(f"{n}x{i}={n*i}")
        print("That's all folkes!")
    elif opt == 4:
        break

    else:
        print("Whoooopsie! - no such option. Try again.")


def shop():
    """
    Returns a dictionary of items available in the shop with their prices
    """
    items = {
        "ipod": 500.00,
        "mouse": 9.99,
        "potatoes": 1.99,
        "python tuition": 0.99,
        "carrot": 0.29
    }
    return items


def basket():
    """
    Allows the user to add items and quantities to their basket
    Returns a list containing all selected items
    """
    b = []  # empty list to store basket items
    while True:
        item = input('Enter next item or "STOP" to stop: ').lower()

        # stop condition
        if item.upper() == "stop":
            break
        # ask for quantity
        q = int(input(f"Enter the quantity of {item}: "))
        # add item q times to the basket
        for i in range(q):
            b.append(item)

    return b


def till(basket):
    """
    Calculates the total cost of all items in the basket
    """
    all_items = shop()   # dictionary of shop items
    total = 0.0          # total price

    for product in basket:
        if product in all_items:
            total += all_items[product]
        else:
            print(f"Sorry mate, the {product} is not available. Go to Lidl")

    return total

# ---------- MAIN PROGRAM ----------
my_basket = basket()
final_total = till(my_basket)
print(f"Total to pay: £{final_total:.2f}")