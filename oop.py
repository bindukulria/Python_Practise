class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def display (self):
          print("length:", r1.length)
          print("width:", r1.width)
          print("area:", r1.area())
          print("perimeter:", r1.perimeter())
    
    
#create object
r1= Rectangle(10, 5)

r1.display()

