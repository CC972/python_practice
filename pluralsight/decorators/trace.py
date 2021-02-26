"""Instance decorator"""


class Trace:
    """Class which prints out information each time it's called.
    This can be toggled on and off."""

    def __init__(self):
        self.enabled = True

    def __call__(self, f):

        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap


# It is the instance of the class, and not the class itself, which is the decorator
tracer = Trace()


@tracer
def rotate_list(l):
    """Shift each element in the list left by one """
    return l[1:] + [l[0]]


l = [1, 2, 3]

l = rotate_list(l)
print(l)

tracer.enabled = False

l = rotate_list(l)  # No longer prints anything when enabled set to False
print(l)

