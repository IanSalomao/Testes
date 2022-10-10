from pytest import mark
from Standard_Structure_Test import standard_structure_for_quadrant_test


def test_must_get_the_first_quadrant_by_the_coordinate():
    standard_structure_for_quadrant_test(2, 2, "First")


def test_must_get_the_fourth_quadrant_by_the_coordinate():
    standard_structure_for_quadrant_test(3, -2, "Fourth")


def test_must_get_the_third_quadrant_by_the_coordinate():
    standard_structure_for_quadrant_test(-8, -1, "Third")


def test_must_get_the_second_quadrant_by_the_coordinate():
    standard_structure_for_quadrant_test(-7, 1, "Second")


def test_must_get_the_null_quadrant_by_the_coordinate():
    standard_structure_for_quadrant_test(0, 2, "")


@mark.xfail
def test_not_must_get_the_quadrant_by_the_coordinate_Xfail():
    standard_structure_for_quadrant_test("A", 0, "")
