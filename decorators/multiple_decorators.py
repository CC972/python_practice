"""Combining decorators"""


def escape_unicode(f):

    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x.encode('unicode-escape').decode('ascii')

    return wrap


class Trace:

    def __init__(self):
        self.enabled = True

    def __call__(self, f):

        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap


tracer = Trace()


@tracer
@escape_unicode
def norwegian_island_maker(name):
    """Return made-up names of Norwegian islands"""

    return name + 'øy'


print(norwegian_island_maker('Llama'))

tracer.enabled = False

print(norwegian_island_maker('Python'))
