#getting user input for temp in C
temperature = float(input("What is the temperature in Celsius? "))
#converting to Fahrenheit
temp_fahrenheit = (temperature * 9 / 5) + 32

print(f"{temperature} Celsius degrees is {temp_fahrenheit} Fahrenheit degrees.")