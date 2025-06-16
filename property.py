class Circle:
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def area(self):
        return self.PI * self.radius * self.radius
    
    @area.setter
    def area(self, value):
        self.radius = value
    
    @area.deleter
    def area(self):
        del self.radius

circle = Circle(5)
print(circle.area)
circle.area = 10
print(circle.area)
del circle.area