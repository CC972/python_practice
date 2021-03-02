import math


class InclinationError(Exception):
    pass


def inclination(dx, dy):
    """Returns slope in degrees given the horizontal and vertical components of a distance"""

    try:
        return math.degrees(math.atan(dy / dx))
    except ZeroDivisionError as e:
        # Associate original ZeroDivisionError exception with new InclinationError exception via __cause__ attribute
        # Effectively translating one into another
        raise InclinationError("Slope cannot be vertical") from e


# Case where horizontal component is non-zero
print(inclination(3, 5))

# Case where horizontal component is zero
try:
    print(inclination(0, 5))
except InclinationError as e:
    print(e)
    print(e.__cause__)
