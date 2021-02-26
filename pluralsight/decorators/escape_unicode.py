"""Function decorator"""


def escape_unicode(f):
    """Decorator to convert non-ASCII characters to escape sequences"""

    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    # Returns callable wrap(), which uses closure to access f after escape_unicode returns
    return wrap


@escape_unicode
def northern_city():
    return 'Tromsø'


print(northern_city())
