class Position:

    def __init__(self, latitude, longitude):
        # Validating invariants
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")

        self._latitude = latitude
        self._longitude = longitude

    # Read-only properties
    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"

    # Instance method, so accepts self
    # repr() is intended for developers, should nearly always override
    # Good practice to include necessary state and to format it such that it looks like a constructor call
    def __repr__(self):
        # Use typename instead of hard-coding Position so that it will work with inheritance
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})"

    # Default implementation of __str__ delegates to __repr__
    # Need to override to customize behaviour
    # str() is generally intended for consumers of system (users, people, UIs, other systems, etc.)
    # Should be readable and leave out technical implementation details
    def __str__(self):
        # Convention that default format invocation where format_spec is the empty string gives same result as __str__
        # So let __str__ delegate to __format__ via built-in format function without second argument
        return format(self)

    # Default implementation of __format__ delegates to __str__
    def __format__(self, format_spec):
        component_format_spec = ".2f"
        # Use partition method of str class to parse format spec into 3 parts
        prefix, dot, suffix = format_spec.partition(".")
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f".{num_decimal_places}f"
        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return (
            f"{latitude}° {self.latitude_hemisphere}, "
            f"{longitude}° {self.longitude_hemisphere}"
        )

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return (self.latitude == other.latitude) and (self.longitude == other.longitude)

    def __hash__(self):
        return hash((self.latitude, self.longitude))


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


# Utility function to get name of class
def typename(obj):
    return type(obj).__name__


# Without implementing custom repr(), str() and format() methods
# Would just get the inherited string conversion behaviour from the object base class
# When printing the object instance itself, Python requests the repr of the result (hence intended for developers)
sydney = Position(-33.9, 151.2)
print(sydney)
r = repr(sydney)  # String
print(type(r))
p = eval(r)  # Use eval to evaluate string as if it were source code, results in second Position object
print(p)

# Demonstrating how repr() extends to work with subclasses
mauna_kea = EarthPosition(19.82, -155.47)
print(mauna_kea)
olympus_mons = MarsPosition(18.65, -133.8)
print(olympus_mons)

# Testing out str()
mount_erebus = EarthPosition(-77.5, 167.2)
print(str(mount_erebus))
print("Mount Erebus is located at",  mount_erebus)

# Testing out format(), which is also used by f strings
matterhorn = EarthPosition(45.9763, 7.6586)
print(format(matterhorn))
print(format(matterhorn, ".1"))
print(f"The Matterhorn is at {matterhorn:.3}")

# Formatting example with floats where format() delegates to __format__
q = 7.748091e-5
print(format(q))
print(format(q, "f"))  # Fixed point representation
print(format(q, ".7f"))  # Specify number of decimal places
print(format(q, "+.11f"))  # Explicit positive number sign
print(format(q, ">+20"))  # Right-align number to field width of 20
print(f"The conductance quantum is {q:.6f}")
print(f"The conductance quantum is {q:.2e}")

# Can force use of __str__ or __repr__
everest = EarthPosition(27.988056, 86.925278)
print(f"The everest object is {everest!r}")
print(f"Mount Everest is at {everest!s}")
print(f"{everest=}")  # Displays __repr__ result
