class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def display(self):
        print ("Length of Rectangle is: ", self.length)
        print ("Breadth of Rectangle is: ", self.breadth)
        
    def area(self):
        return (self.length*self.breadth)
    
    def perimeter(self):
        return (2*self.length + 2*self.breadth)
    
l = int (input("Enter the length of the Rectangle: "))
b = int (input("Enter the breadth of rectangle: "))

print("Length of small rectangle:")
smallLength = int(input())
print("Breadth of small rectangle:")
smallBreadth = int(input())
smallRectangle = Rectangle(smallLength,smallBreadth)

print("Area: ",smallRectangle.area())
print("Perimeter: ",smallRectangle.perimeter())

print("Length of large rectangle:")
largeLength = int(input())
print("Breadth of large rectangle:")
largeBreadth = int(input())
largeRectangle = Rectangle(largeLength,largeBreadth)

print("Area: ",largeRectangle.area())
print("Perimeter: ",largeRectangle.perimeter())