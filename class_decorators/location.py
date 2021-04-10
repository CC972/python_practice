import inspect
from object_orientation.position import EarthPosition, typename


# Class decorators accept a class and return a class
def auto_repr(cls):

    # Request members of class
    # Returns mapping from member names to member objects
    members = vars(cls)

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} already defines __repr__")

    # Check that class implements its own initializer
    # Members mapping does not include inherited members
    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    # Need to verify that for every argument after self, there exists a property with the same name
    # First get argument list of __init__ by passing reference to __init__ method of signature function
    # Note we are not calling __init__ here, just passing it in as an argument
    sig = inspect.signature(cls.__init__)

    # Get all parameter names except first, which is self
    parameter_names = list(sig.parameters)[1:]

    if not all(  # Since need to ensure every argument has a matching property (i.e. all evaluate to True)
        # Attempt to get property corresponding to each member name after self via generator expression
        # Evaluates to a series of Boolean values
        isinstance(members.get(name, None), property)
        for name in parameter_names
    ):
        raise TypeError(
            f"Cannot apply auto_repr to {cls.__name__} because not all "
            "__init__ parameters have matching properties"
        )

    # Define local method within class decorator
    # So we can close over useful variables already defined (e.g. parameter names)
    def synthesized_repr(self):
        return "{typename}({args})".format(
            # Get typename of self instead of cls
            # Because want __repr__ to report the runtime dynamic type of self, not the static type class
            typename=typename(self),
            args=", ".join(
                "{name}={value!r}".format(
                    name=name,
                    value=getattr(self, name)  # Retrieve property value
                ) for name in parameter_names  # Generator expression
            )
        )

    # Set __repr__ to synthesized_repr
    setattr(cls, "__repr__", synthesized_repr)

    return cls


@auto_repr  # Decorator to synthesise __repr__ method of class
class Location:

    def __init__(self, name, position):

        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __str__(self):
        return self.name


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))

print(repr(hong_kong))
