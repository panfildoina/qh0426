from Human import Human
from Robot import Robot

class Planet:
    
    def __init__(self, name):
        self.name = name
        self.inhabitants = {
            'humans' : [],
            'robots' : []
        }
        
    def __repr__(self):
        return f"planet(humans={self.inhabitants['humans']}, robots={self.inhabitants['robots']})"
    
    def __str__(self):
        return f"this planet has {len(self.inhabitants['humans'])} humans and {len(self.inhabitants['robots'])} robots"
    
    def add_human(self, human):
        self.inhabitants['humans'].append(human)
        
    def add_robot(self, robot):
        self.inhabitants['robots'].append(robot)
        

if __name__ == '__main__':
    planet = Planet("Earth")
    print(repr(planet))
    
    h = Human("Sha")
    planet.add_human(h)
    print(repr(planet))
    print(planet)
    
    r = Robot("T-100")
    planet.add_robot(r)
    print(repr(planet))
    print(planet)