from home_work.classes.Figure import Figure
from math import pi as PI


class Circle(Figure):
    name = 'Круг'
    angles = None

    def __init__(self, radius):
        # Figure.__init__(self)
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError('Значение радиуса должно быть больше 0')

    def perimeter(self):
        return 2 * PI * self.radius

    def area(self):
        return PI * self.radius ** 2
