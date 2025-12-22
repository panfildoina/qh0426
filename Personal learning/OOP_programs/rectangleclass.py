class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self. width = width 
    def area(self):
        return self.length * self.width 
    
    def perimeter(self):
        return 2 * (self.length + self.width)
#testing the class
rect1 = Rectangle(5,4)
print(f"The area of the rectangle is {rect1.area()}")
print(f"The perimeter of the rectangle is  {rect1.perimeter()}")
