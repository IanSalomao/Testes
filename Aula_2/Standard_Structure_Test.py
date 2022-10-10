from Coordinate import Coordinate
from Quadrant import Quadrant


def standard_structure_for_quadrant_test(cordinate_x, cordinate_y, output):
    # Arrange
    coordinates = Coordinate(cordinate_x, cordinate_y)
    quadrant = Quadrant(coordinates)

    # Action
    result = quadrant.get_quadrant_coordinate()

    # Assert
    assert result == output
