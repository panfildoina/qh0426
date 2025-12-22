#creating a tuple of likelihood values and returning the smallest
def likelihood():
    likelihood_values = (50,38,27,99,4)
    return min(likelihood_values)

#this fuctions calles likelihood functions, stores the result and displays the result  
def run_task1():
    smallest_value = likelihood() #calling the first function
    print(f"Minimum likelohood of falling: {smallest_value}%")

#Run the program only when executed directly
if __name__ == "__main__":
    run_task1()
    
#program 2 Find both minimum and maximum
#creating a tuple of likelihood values and getting the min and max
def likelihood_min_max():
    #populating with values
    likelihoods =(50, 38, 27, 99, 4)
    #finding the min and max value
    minimum = min(likelihoods)
    maximum = max(likelihoods)
    #retruning both values
    return minimum, maximum
#calling the likelihood_max_min, storing return values
#printing the result in requested format

def run_task2():
    min_value,max_value = likelihood_min_max()

    print(f"The minimum likelihood of failing: {min_value}%")
    print(f"The maximum likelihood of failing: {max_value}%")
# Run the program only when executed directly
if __name__ == "__main__":
    run_task2()

#Program 3
# Creating a list containing tuples (step name, likelihood)

def steps():
    likelihoods = [("step 1", 50),
                   ("step 2", 38),
                   ("step 3", 27), 
                   ("step 4", 99),
                   ("step 5", 4)
                   ]
    return likelihoods
# separating steps into good and bad based on likelihood threshold
def run_task3():
    # Retrieve the list of tuples from steps()
    step_list = steps()
    # Create empty lists for good and bad steps
    good_steps = []
    bad_steps = []
    #Loop through each tuple in the list 
    for step_name, likelihood in step_list:
        if likelihood >= 50:
            bad_steps.append((step_name, likelihood))
        else:
            good_steps.append((step_name, likelihood))
  
    # Display final counts
    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")


# Ensure the program runs only when executed directly
if __name__ == "__main__":
    run_task3()



