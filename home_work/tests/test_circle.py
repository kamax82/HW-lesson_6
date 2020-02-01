import pytest
from home_work.classes.Circle import Circle

cir_a = Circle(27)
cir_b = Circle(137.25)
not_cir = {'Hello': 'world'}


def test_circle_name():
    assert cir_a.name == 'Круг'


def test_circle_angles():
    assert cir_a.angles == None


def test_circle_perimeter():
    assert round(cir_a.perimeter(), 1) == 169.6
    assert round(cir_b.perimeter(), 1) == 862.4


def test_circle_area():
    assert round(cir_a.area(), 1) == 2290.2
    assert round(cir_b.area(), 1) == 59179.9


def test_circle_add_square_pos():
    assert round(cir_a.add_square(cir_b), 1) == 61470.2


def test_circle_add_square_neg():
    '''Should raise a ValueError because not_cir is not a figure'''
    with pytest.raises(ValueError):
        assert cir_a.add_square(not_cir)


def test_circle_creation_neg():
    '''Should raise a ValueError because wrong_cir can't exist'''
    with pytest.raises(ValueError):
        wrong_cir = Circle(-55.3)
