class Shape:
    name = "Shape"
    def get_area(self):
        pass
    def get_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        area = 0
        area = 3.14 * self.radius ** 2
        return area
    
    def get_perimeter(self):
        perimeter = 0
        diameter = self.radius * 2
        perimeter = diameter * 3.14
        return perimeter

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def get_area(self):
        area = 0
        area = self.length * self.width
        return area
    
    def get_perimeter(self):
        perimeter = 0
        perimeter = 2 * (self.length + self.width)
        return perimeter


def main():
    cnew = Circle(10)
    print("Area of Circle: ", cnew.get_area())
    print("Perimeter of Circle: ", cnew.get_perimeter())
    
    rnew = Rectangle(10, 20)
    print("Area of Rectangle: ", rnew.get_area())
    print("Perimeter of Rectangle: ", rnew.get_perimeter())


main()
    