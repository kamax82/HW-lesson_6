import pytest
from home_work.classes.Square import Square

sq_a = Square(12)
sq_b = Square(6.5)
not_sq = 'Hello'


def test_square_name():
    assert sq_a.name == 'Квадрат'


def test_square_angles():
    assert sq_a.angles == 4


def test_square_perimeter():
    assert sq_a.perimeter() == 48
    assert sq_b.perimeter() == 26


def test_square_area():
    assert sq_a.area() == 144
    assert sq_b.area() == 42.25


def test_square_add_square_pos():
    assert sq_a.add_square(sq_b) == 186.25


def test_square_add_square_neg():
    '''Should raise a ValueError because not_sq is not a figure'''
    with pytest.raises(ValueError):
        assert sq_a.add_square(not_sq)


def test_square_creation_neg():
    '''Should raise a ValueError because wrong_sq can't exist'''
    with pytest.raises(ValueError):
        wrong_sq = Square(-3)
