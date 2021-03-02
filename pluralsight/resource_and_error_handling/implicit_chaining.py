import sys
import io

from user_defined_exceptions import triangle_area, TriangleError


# Demonstrate implicit exception chaining by introducing two bugs below
def main():

    try:
        a = triangle_area(3, 4, 10)  # First bug: trying to evaluate area of non-triangle
        print(a)
    except TriangleError as e:
        print(e, file=sys.stdin)  # Second bug: trying to print to standard in stream instead of standard error stream


# Modify code to see how the chaining works
def main():

    try:
        a = triangle_area(3, 4, 10)
        print(a)
    except TriangleError as e:
        try:
            print(e, file=sys.stdin)
        except io.UnsupportedOperation as f:
            print(e)  # TriangleError
            print(f)  # UnsupportedOperation
            # The TriangleError gets attached to the __context__ attribute of the UnsupportedOperation exception object
            print(f.__context__ is e)


main()
