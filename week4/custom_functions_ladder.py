def climb_ladder(steps_remaining, steps_crossed):
    if steps_remaining > steps_crossed:
        print("Still same way to get")
    else:
        print("We are almost there....")
    
steps_re = int(input("Eneter the steps remaining: "))
steps_cr = int(input("Enter the steps crossed: "))
climb_ladder(steps_re, steps_cr)

#climb_ladder(steps_re, steps_cr)

