#create a class Person with atributes name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
#add method that outputs "Hello my name is and I am x years old."
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
#testing it
john = Person("John", 25)
john.introduce()
