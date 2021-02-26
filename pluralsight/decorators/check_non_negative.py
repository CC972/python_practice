"""Demonstrating how parametrised decorators can be used for argument validation"""


def check_non_negative(index):
    """Verify function arguments are non-negative"""

    def validator(f):
        """Nested decorator"""

        def wrap(*args):
            if args[index] < 0:
                raise ValueError('Argument at index {} must be non-negative'.format(index))
            return f(*args)
        return wrap  # Forms closure over the decorated function f, as well as the index

    return validator


# Use decorator to check second argument of function is not negative
@check_non_negative(1)  # Calling returns the decorator itself
def create_list(value, size):
    return [value] * size


print(create_list('a', 3))
print(create_list('a', -5))
