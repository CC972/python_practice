i = 7
print(type(i))
print(int)
print(repr(int))
print(type(i) is int)
print(type(i)(78))
type(type(i))
print(i.__class__)
print(i.__class__.__class__)  # Type is its own type
print(i.__class__.__class__.__class__)

# issubclass() determines if first argument is a subclass of second
# Second argument can be a single class or a tuple of classes
print(issubclass(type, object))
print(type(object))

# isinstance() determines if first argument is an instance of a class
# First argument can be object of any type
# Second argument can be a single class or a tuple of classes
print(isinstance(i, int))

# In general type tests should be avoided
# However when type checks are necessary, prefer isinstance() and issubclass() over direct comparison of type objects
