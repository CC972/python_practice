"""Demonstrating how the original function's metadata can be preserved when using decorators"""

import functools


def hello():
    """Prints Hello World"""

    print("Hello, world!")


# Attributes such as the below are used by tools like debuggers and IDEs
print(hello.__name__)
print(hello.__doc__)

print(help(hello))


def noop(f):

    def noop_wrapper():
        return f()

    return noop_wrapper


@noop
def hello():
    """Prints Hello World"""

    print("Hello, world!")


# With the decorator in place, the information provided is no longer as informative as before
# Since the information is now about the wrapper function used by the decorator
print(hello.__name__)
print(hello.__doc__)

print(help(hello))


def noop(f):

    def noop_wrapper():
        return f()

    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__

    return noop_wrapper


@noop
def hello():
    """Prints Hello World"""

    print("Hello, world!")


# Now the metadata from the original function is preserved
print(hello.__name__)
print(hello.__doc__)

print(help(hello))


# A more elegant solution is to use functools.wraps()
def noop(f):

    @functools.wraps(f)
    def noop_wrapper():
        return f()

    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__

    return noop_wrapper


@noop
def hello():
    """Prints Hello World"""

    print("Hello, world!")


print(hello.__name__)
print(hello.__doc__)

print(help(hello))
