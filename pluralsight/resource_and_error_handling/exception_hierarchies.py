# Use __mro__ (Method Resolution Order) to retrieve transitive base classes of a class
# IndexError and KeyError are siblings in the class hierarchy as both are immediate subclasses of LookUpError
# In practice this means we can catch both error types by catching LookupError
print(IndexError.__mro__)
print(KeyError.__mro__)


def lookups():

    s = [1, 4, 6]

    try:
        item = s[5]
    except IndexError:  # Could replace with LookupError
        print("Handled IndexError")

    d = dict(a=65, b=66, c=67)

    try:
        value = d['x']
    except KeyError:  # Could replace with LookupError
        print("Handled KeyError")


lookups()
