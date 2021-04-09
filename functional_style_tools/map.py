import itertools

# Find Unicode code points for each character in a string
# Returns a map object since map() performs lazy evaluation
# Map object returned is an iterator object (lazy), which only by iterating over are the values produced
print(map(ord, 'The quick brown fox'))


class Trace:

    def __init__(self):
        self.enabled = True

    def __call__(self, f):

        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)

        return wrap


result = map(Trace()(ord), 'The quick brown fox')
print(result)

# Usually would not manually drive a map object (i.e. using next())
# More common to iterate over it using a higher-level method
print(list(map(ord, 'The quick brown fox')))

# Using map() with multiple iterables
# Need as many input sequences as there are arguments in the mapping function
sizes = ['small', 'medium', 'large']
colors = ['lavender', 'teal', 'burnt orange']
animals = ['koala', 'platypus', 'salamander']


def combine(size, color, animal):
    return '{} {} {}'.format(size, color, animal)


print(list(map(combine, sizes, colors, animals)))


# Input sequences do not all have to be the same size
def combine(quantity, size, color, animal):
    return '{} x {} {} {}'.format(quantity, size, color, animal)


# Passing an infinite sequence to demonstrate that map() terminates once any of the sequences are exhausted
print(list(map(combine, itertools.count(), sizes, colors, animals)))
