#importing the module I created
import math_operations 
result = math_operations.add(8, 5)
print(result)
#importing specific opeations
from math_operations import add, substract 
print(add(5,3)) 
print(substract(10,8))

#Alias in Modules (giving a different name to the module when importing it)
import math_operations as mo 
print(mo.add(8,9))


#built-in Modules 
import os
import math

print(math.sqrt(16)) #output will be 4 
print(os.getcwd()) #output will be current directory
