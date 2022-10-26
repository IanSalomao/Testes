from Coordinate import Coordinate
from Quadrant import Quadrant
from pytest import mark

def test_must_get_the_quadrant_by_the_coordinate():
    # Arrange
    coordinate1 = Coordinate(2, 2)
    quadrant1 = Quadrant(coordinate1)

    coordinate2 = Coordinate(3, -2)
    quadrant2 = Quadrant(coordinate2)

    coordinate3 = Coordinate(-8, -1)
    quadrant3 = Quadrant(coordinate3)

    coordinate4 = Coordinate(-7, 1)
    quadrant4 = Quadrant(coordinate4)

    coordinate5 = Coordinate(0, 2)
    quadrant5 = Quadrant(coordinate5)

    # Action
    result1 = quadrant1.get_quadrant_coordinate()
    result2 = quadrant2.get_quadrant_coordinate()
    result3 = quadrant3.get_quadrant_coordinate()
    result4 = quadrant4.get_quadrant_coordinate()
    result5 = quadrant5.get_quadrant_coordinate()

    # Assert
    assert result1 == "First"
    assert result2 == "Fourth"
    assert result3 == "Third"
    assert result4 == "Second"
    assert result5 == ""


@mark.xfail
def test_not_must_get_the_quadrant_by_the_coordinate_Xfail():
    # Arrange
    coordinate = Coordinate("A", 2)
    quadrant = Quadrant(coordinate)

    #Act
    result = quadrant.get_quadrant_coordinate()

    #Assert
    assert result