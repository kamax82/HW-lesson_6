from home_work.classes.Rectangle import Rectangle


class Square(Rectangle):
    name = 'Квадрат'

    def __init__(self, size_a):
        # Rectangle.__init__(self)
        if size_a > 0:
            self.size_a = size_a
            self.size_b = self.size_a
        else:
            raise ValueError('Значение сторон должно быть больше 0')
