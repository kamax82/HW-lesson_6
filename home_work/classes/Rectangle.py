from home_work.classes.Figure import Figure


class Rectangle(Figure):
    name = 'Прямоугольник'
    angles = 4

    def __init__(self, size_a, size_b):
        if size_a > 0 and size_b > 0:
            self.size_a = size_a
            self.size_b = size_b
        else:
            raise ValueError('Значение сторон должно быть больше 0')

    def perimeter(self):
        return (self.size_a + self.size_b) * 2

    def area(self):
        return self.size_a * self.size_b
