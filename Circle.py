from turtle import circle


class Circle:
    PI = 3.14
    circle_list = []

    def __init__(self, radius):
        self.radius = radius
        self.circle_list.append(self)

    def area (self):
        return self.PI * self.radius ** 2

    def perimeter (self):
        return self.radius * 2 * self.PI

Area = Circle(10)
Perimeter = Circle(10)

print('Area of a Circle = ',Area.area())
print('Perimeter of a Circle = ',int(Perimeter.perimeter()) )