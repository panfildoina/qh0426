#creating a list of fruits and print each fruit capitalize
fruits = ['apple', 'banana', 'cherry', 'orange']
for fruit in fruits:
    print(fruit.upper())

#creating a list of fruits and print each fruit capitalize
vegetables = ['tomato', 'onion', 'potato', 'eggplant']
for vegetable in vegetables:
    print(vegetable.upper())

#creating a dictionary and printing each key-value pair in formatted sentence:

countries = {'USA': 'Washington, D.C', 'France': 'Paris', 'Japan': 'Tokyo'}
for country, capital in countries.items():
    print(f"The capital of {country} is  {capital}.")

#looping through numbers and printing each number multiplied by 2

numbers = {1, 2, 3, 4, 5}
for number in numbers:
    print (number * 2)