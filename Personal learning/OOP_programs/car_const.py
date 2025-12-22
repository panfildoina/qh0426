
#creating car class with methods: start, accelerate and stop
class Car:
    def start(self):
        print("Starting the car.")
    
    def accelerate(self):
        print("Accelerating the car.")

    def stop(self):
        print("Stopping the car.")
#testing the clas
my_car = Car()
my_car.start()
my_car.accelerate()
my_car.stop()

#implementing attributes and making them private

class Car:
    def __init__(self):
        self.__speed = 0
    def start(self):
        self.__speed = 20
        print(f"Starting the car. The speed is {self.__speed} mph")
    def accelerate(self):
        self.__speed +=20
        print(f"Accelerating the car. The speed  is now {self.__speed} mph")
    def stop(self):
        self.__speed = 0
        print(f"The car is stopped. Speed is now {self.__speed} mph")

#creating Subclass electrical car, overide accelerate method to display accelerating silently
class ElectricCar(Car):
    def accelerate(self):
        print("Accelerating silently")
#testing
my_electric_car = ElectricCar()
my_electric_car.start()
my_electric_car.accelerate()
my_electric_car.stop()

