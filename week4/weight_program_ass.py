def sum_weights(person_weight, inventory_weight):
    total_weight =  person_weight + inventory_weight 
    return total_weight

def calc_avg_weight(person_weight, inventory_weight):
    avg_weight = sum_weights(person_weight, inventory_weight) / 2
    return avg_weight

def run():
    #retrieve user input
    person_weight = float(input("What is the weight of the person?\n"))
    print()
    inventory_weight = float(input("What is the weight of the invetory?\n"))
    print()
    action = input("What would you like to calculcate (sum or average)?\n")

    #determine and carry out action
    if action == "sum":
        answer = sum_weights(person_weight, inventory_weight)
        print(f"The sum of weights is {answer:.2f}")
    elif action == "average":
        answer = calc_avg_weight(person_weight, inventory_weight)
        print(f"The average weight is {answer:.2f}")
    else:
        print("I am not sure what would you like to do")

#call the function
run()
 
 