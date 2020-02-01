from abc import ABC
from abc import abstractmethod


class Figure(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def add_square(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.area() + other_figure.area()
        else:
            raise ValueError('Заданные объект не принаддлежит классу фигур')
