def shop():
    items = {"ipod": 500, "mouse": 9.99, "potatoes": 1.99, "python tuition": 0.99, "carrot": 0.29}
    return items

def basket():
    b = []
    while True:
        item = input("Enter next item or \"stop\" to stop: ")
        if item.upper() == "STOP":
            break
        q = int(input(f"Enter the quantity of {item}: "))
        for i in range(q):
            b.append(item.lower())
    return b

def till(basket = []):
    all_items = shop()
    total = 0.0
    for product in basket:
        if product in all_items:
            total += all_items[product]
        else:
            print(f"Sorry mate, the {product} is not available. Go to Lidl")
    return total

