weight = float(input("Enter your weight "))
unit = input("Kilograms or Pounds? Kg/Lb: ")

if unit.upper() == "KG":
    converted_weight = weight * 2.205 

elif unit.upper() == "LB":
    converted_weight = weight / 2.205
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {round(converted_weight, 2)}{unit}")


