class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter
    
    def area(self):
        area = self.length * self.width
        return area
    
    def display(self, area, perimeter):
        print(f"The rectangle properties: Length {self.length}  Width {self.width}")
        print(f"Perimeter {perimeter}")
        print(f"Area {area}")


reectangle = Rectangle(3, 8)
reectangle.display(reectangle.area(), reectangle.perimeter())
