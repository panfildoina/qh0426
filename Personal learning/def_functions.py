#function that is reversing a string
def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello"))

#fuction that takes 2 numbers as aruguments
def sum_two_numbers(a,b):
    return a + b
#Test the function
print(sum_two_numbers(5,10))

#average of a list numbers
def average (numbers):
    return sum(numbers) / len(numbers)
print(average([1, 2, 3, 4, 5]))

def greet_world():
    print("Hello World!")
greet_world()

#Converting Fahreinheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit -32) * 5/9, 2)
print(fahrenheit_to_celsius(54))

#sorting numbers
def sort_list(nums):
    return sorted(nums)
print(sort_list([2, 9, 0, 1, 6 , 7]))
#or manually 
def sort_list(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
print(sort_list([2, 9, 0, 1, 6 , 7]))
print(sort_list([2, 119, 20, 13, 16 , 7]))


#Calculating circle radius
#A = pi * r^2
import math #need to access pi value
def circle_area(radius):
    return round(math.pi * (radius ** 2),2)

#Test the function:

print(circle_area(5))
print(circle_area(10))