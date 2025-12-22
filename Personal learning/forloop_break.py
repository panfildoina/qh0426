#Calculating the sum from 1 t0 101 and breaking when the sum reaches over 500
total_sum = 0
for sum in range(1, 101):
    total_sum += sum
    if total_sum > 500:
        print(f"The sum reached {total_sum} at sum = {sum}. Breaking the loop.")
        break     
    


