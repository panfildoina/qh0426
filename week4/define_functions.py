def cross_bridge(steps):
    for i in range(2, steps):
        print(f"Crossed step {i} ")
    
    if steps > 5:
        print("The bridge is collapsing...")
    else:
        print("We must keep going")

cross_bridge(4)
cross_bridge(7)
