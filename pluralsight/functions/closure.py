def enclosing():
    x = 'Closed over'

    def local_func():
        print(x)

    return local_func


lf = enclosing()
print(lf())

# Closure refers to single object:
# The x variable defined in the function which defined lf
print(lf.__closure__)


def raise_to(exp):
    """Function factory for raising a number to a particular power."""

    def raise_to_exp(x):
        return pow(x, exp)

    return raise_to_exp


square = raise_to(2)
print(square.__closure__)
print(f"Square of 5: {square(5)}")

cube = raise_to(3)
print(cube.__closure__)
print(f"Cube of 5: {cube(5)}")
