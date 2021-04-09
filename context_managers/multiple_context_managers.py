import contextlib


@contextlib.contextmanager
def nest_test(name):

    print('Entering', name)
    yield name
    print('Exiting', name)


with nest_test('outer'), nest_test('inner'):
    print('BODY')

# Equivalent to the above form
with nest_test('outer'):
    with nest_test('inner'):
        print('BODY')

# Later context managers are simply part of the body as far as the earlier context managers are concerned
# Names bound in an as clause in earlier parts of the with statement can be used when defining later context managers
with nest_test('outer') as n1, nest_test('inner, nested in ' + n1):
    print('BODY')


@contextlib.contextmanager
def propagator(name, propagate):
    """Simple context manager which can be configured to either propagate or swallow exceptions"""

    try:
        yield
        print(name, 'exited normally')
    except Exception:
        print(name, 'received an exception')
        if propagate:
            raise


# If an inner context manager swallows an exception, it won't be seen by outer context managers
with propagator('outer', True), propagator('inner', False):
    raise TypeError()

# Likewise, exceptions propagated from inner context managers will be seen by outer context managers
with propagator('outer', False), propagator('inner', True):
    raise TypeError()

# Can use line continuation (or nesting) if using multiple context managers
with nest_test('a'), \
     nest_test('b'), \
     nest_test('c'):
    pass
