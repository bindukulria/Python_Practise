from quadrila import Quadrilateral 

class Rectangle(Quadrilateral):#parent class is Quadrilateral

    count=0

    def __init__(self,length,breadth):
        Rectangle.count += 1
        super().__init__(length,breadth,length,breadth)

        self.id = Rectangle.count
        self.length = length
        self.breadth = breadth

    def area(self):
            print("I am area of Rectangle")
            return self.length * self.breadth
    def perimeter(self):
          return 2 * (self.length + self.breadth)
        
    def __add__(self,r):
            print("I am method of Rectangle")
            return self.area() >= r.area()

    def __str__(self):
            return f"Rectangle ID: {self.id} Dimension is {self.length}X{self.breadth}"

r1 = Rectangle(10,5)

print(r1.area())
print(r1)










