class Robot:
    
    #class atrribute
    laws = "Protect, Obey and Survive"

    #static methos
    @staticmethod
    def the_law():
        print(Robot.laws)


    #class method
    @classmethod
    def assemble(cls):
        return cls("Aseembled Robot")
    
    #instance
    def __init__(self, name = "Robot"):
        #an instant attribute
        self.name = name
        self.age = 0 
    
    def display(self):
        print(f" The {selfname}")

    def run():
        rob = Robot()
        print(rob.display())
        print(rob.assemple())
        print(rob.the_law())



if __name__ =="__main__":
    run()
