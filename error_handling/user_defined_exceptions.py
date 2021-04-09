import math


# Define domain-specific error, which should inherit from Exception rather than BaseException
class TriangleError(Exception):

    def __init__(self, text, sides):
        super().__init__(text)
        self._sides = tuple(sides)  # Store as tuple to prevent modification

    # Read-only attribute to access sides
    @property
    def sides(self):
        return self._sides

    def __str__(self):
        return "'{}' for sides {}".format(self.args[0], self._sides)

    def __repr__(self):
        return "TriangleError({!r}, {!r})".format(self.args[0], self._sides)


def triangle_area(a, b, c):
    """Use Heron's formula to compute the area of a triangle"""

    sides = sorted((a, b, c))
    if sides[2] > sides[0] + sides[1]:
        raise TriangleError("Illegal triangle", sides)

    p = (a + b + c) / 2
    a = math.sqrt(p * (p - a) * (p - b) * (p - c))

    return a


# Valid side lengths
print(triangle_area(3, 4, 5))

# Invalid side lengths
try:
    triangle_area(3, 4, 10)
except TriangleError as e:
    print(e.sides)
