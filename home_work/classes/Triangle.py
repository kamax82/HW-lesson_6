from home_work.classes.Figure import Figure
import math


class Triangle(Figure):
    name = 'Треугольник'
    angles = 3

    def __init__(self, size_a, size_b, angle_a):
        # Figure.__init__(self)
        if size_a > 0 and size_b > 0 and (angle_a > 0 and angle_a < 180):
            self.size_a = size_a
            self.size_b = size_b
            self.angle_a = angle_a
            self.angle_r_a = math.radians(self.angle_a)
        else:
            raise ValueError('Значение сторон должно быть больше 0, угол между ними от 0 до 180')

    def perimeter(self):
        self.size_с = math.sqrt(
            (self.size_a ** 2) + (self.size_b ** 2) - 2 * self.size_a * self.size_b * math.cos(self.angle_r_a))
        return self.size_a + self.size_b + self.size_с

    def area(self):
        return 1 / 2 * self.size_a * self.size_b * math.sin(self.angle_r_a)


t = Triangle(6, 8, 25)
print(t.area())
