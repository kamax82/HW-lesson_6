import pytest
from home_work.classes.Rectangle import Rectangle

rec_a = Rectangle(4.2, 5.6)
rec_b = Rectangle(3.75, 55)
not_rec = 112


def test_rectangle_name():
    assert rec_a.name == 'Прямоугольник'


def test_rectangle_angles():
    assert rec_a.angles == 4


def test_rectangle_perimeter():
    assert rec_a.perimeter() == 19.6
    assert rec_b.perimeter() == 117.5


def test_rectangle_area():
    assert rec_a.area() == 23.52
    assert rec_b.area() == 206.25


def test_rectangle_add_square_pos():
    assert rec_a.add_square(rec_b) == 229.77


def test_rectangle_add_square_neg():
    '''Should raise a ValueError because not_rec is not a figure'''
    with pytest.raises(ValueError):
        assert rec_a.add_square(not_rec)


#
def test_rectangle_creation_neg():
    '''Should raise a ValueError because wrong_rec can't exist'''
    with pytest.raises(ValueError):
        wrong_rec = Rectangle(5, 0)
