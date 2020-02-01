import pytest
from home_work.classes.Triangle import Triangle

tr_a = Triangle(12, 25, 98)
tr_b = Triangle(10.5, 17.3, 7.5)
not_tr = ['A', 3, 5, 'z']


def test_triangle_name():
    assert tr_a.name == 'Треугольник'


def test_triangle_angles():
    assert tr_a.angles == 3


def test_triangle_perimeter():
    assert round(tr_a.perimeter(), 1) == 66.2
    assert round(tr_b.perimeter(), 1) == 34.8


def test_triangle_area():
    assert round(tr_a.area(), 1) == 148.5
    assert round(tr_b.area(), 1) == 11.9


def test_triangle_add_triangle_pos():
    assert round(tr_a.add_square(tr_b), 1) == 160.4


def test_triangle_add_triangle_neg():
    '''Should raise a ValueError because not_tr is not a figure'''
    with pytest.raises(ValueError):
        assert tr_a.add_square(not_tr)


def test_triangle_creation_neg():
    '''Should raise a ValueError because wrong_tr can't exist'''
    with pytest.raises(ValueError):
        wrong_tr = Triangle(5, 8, -55)
