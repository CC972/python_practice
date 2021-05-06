a = 42

# dir() returns a list of attribute names for an instance
# Both attributes and method names are returned (since methods are just attributes which are callable)
print(dir(a))

# Retrieve attribute corresponding to attribute name (equivalent to accessing attribute directly)
print(getattr(a, 'denominator'))
print(a.denominator)

# Verify attribute is indeed a method by using callable()
print(getattr(a, 'conjugate'))
print(callable(getattr(a, 'conjugate')))

# Retrieve type of method
print(a.conjugate.__class__.__name__)

# Check if object has an attribute of a given name
print(hasattr(a, 'bit_length'))

# Generally should prefer the more Pythonic EAFP style programming of using exception handlers
# As opposed to the LBLY (Look Before You Leap) style of using type tests and attribute existence tests
# Programs using hasattr() can quickly become messy
# The optimistic approach (try/except) can also be faster than hasattr(), which uses try/except internally anyway
