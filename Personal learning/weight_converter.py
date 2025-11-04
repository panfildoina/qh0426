weight = float(input("Enter your weight "))
unit = input("Kilograms or Pounds? Kg/Lb: ")

if unit == "Kg":
    weight == weight * 2.205 
    unit = "Lbs"
elif unit == "Lb":
    weight = weight / 2.205
    unit ="Kgs"
else:
    print(f"{unit} was not valid")

print(f"Your weight is: round(weight) {unit}")


weight = float(input("What is your weight (in pounds)? "))
weight = weight * 0.45463
print(weight)