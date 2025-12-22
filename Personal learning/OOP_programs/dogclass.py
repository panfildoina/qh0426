class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print("Whoof, whoof")
#instantation - creating an object from the dog class
my_dog = Dog("Buddy", "Golden Retriever")
#my_dog -object or instance of Dog class, Buddy = name, Golden Retriever =breed

#accessing methods and attributes using dot notation
print(my_dog.name) #outputs Buddy
print(my_dog.breed)  #outputs Golden retriver 
my_dog.bark() #outputs Whoof Whoof 
 

 #contructors and destructors
class Dog:
   def __init__(self, name):
      print(f"{name} is born.")
   def __del__(self): #gets executed when an object is destroyed
      print(f"{self.name} is destroyed")