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
        return (
            f"{abs(self.latitude)}° {self.latitude_hemisphere}, "
            f"{abs(self.longitude)}° {self.longitude_hemisphere}"
        )


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
