class Human:
    
    # class attribute
    MAX_ENERGY = 100
    
    #Initializer
    def __init__(self,name = "Human" , age = 0):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY
        
    #Magic methods
    def __repr__(self):
        return f"human(name={self.name}, age={self.age}, energy={self.energy})"
    
    def __str__(self):
        return f"My name is {self.name} and I am {self.age} years old and my energy is {self.energy}"
    
    # instance method
    def display(self):
        print(f"I am {self.name}")
        
    def grow(self):
        self.age += 1
        
    def eat(self, amount):
        protein = self.energy + amount
        if protein > Human.MAX_ENERGY:
            self.energy = Human.MAX_ENERGY
            return protein - self.energy
        else:
            self.energy = protein
            return 0 
        
    def move(self, distance):
        protein = self.energy - distance
        if protein < 0:
            self.energy = 0
            return self.energy - abs(protein)
        else:
            self.energy = protein
            return 0 
        
        
if __name__ == '__main__':
    human = Human()
    print(repr(human))
    human.move(50)
    print(repr(human))
    human.eat(500)
    print(repr(human))