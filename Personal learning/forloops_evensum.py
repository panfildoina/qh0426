#Summing all even number from 0-100
sum_even = 0  #starting value
for sum in range (2, 101, 2):
    sum_even += sum
print("The sum of all even numbers from 1 to 100 is:", sum_even)

#Summing all odd number from 0-101
sum_odd = 0
for sum in range (1, 102, 2):
    sum_odd += sum
print("The sum of all odd numbers from 0 to 101 is:", sum_odd)
