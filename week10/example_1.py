from abc import ABC, abstractmethod

#Parent class
class Animal:
    def eat(self):
        print("This animal is eating")

    #abstract method
    @abstractmethod
    def make_sound(self):
        pass

#child class
class Dog(Animal):
    def bark(self):
        print("This dog is barking")
        

d=Animal
d.eat()  # Inherited method from Animal class
d.bark() # Method from Dog class