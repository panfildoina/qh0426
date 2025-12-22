class Robot:
    
    # Class attribute
    laws = "Protect, Obey and Survive"
    
    # Constant
    MAX_BATTERY = 100
    
    # static method
    @staticmethod
    def the_law():
        print(Robot.laws)
    
    #  Initializer
    def __init__(self, name="Robot", age=0):
        self.name = name
        self.age = age
        self.battery = Robot.MAX_BATTERY
    
    # Instance 
    def display(self):
        print(f"I am {self.name}")
        
    def recharge(self, amount):
        potential_charge = self.battery - amount
        if (potential_charge > Robot.MAX_BATTERY):
            self.battery = Robot.MAX_BATTERY
            return potential_charge - self.battery
        else:
            self.battery = potential_charge
            return 0
        
    def grow(self):
        self.age += 1
        
    def move(self, distance):
        potential_charge = self.battery - distance
        if (potential_charge < 0):
            self.battery = 0
            return self.battery - abs(potential_charge)
        else:
            self.battery = potential_charge
            return 0
    
    def __repr__(self):
        return f"robot(name={self.name}, age={self.age}, energy={self.battery})"
        
if (__name__ == '__main__'):
    robot = Robot()
    
    robot.the_law()
    print(repr(robot))
    
    robot.move(15)
    print(repr(robot))
    
    robot.recharge(20)
    print(repr(robot))
    
    robot.recharge(20)
    print(repr(robot))
    