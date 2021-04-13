from dataclasses import dataclass

from object_orientation.position import Position, EarthPosition


# Optional arguments (among others) to make class equality comparable (i.e. enable __eq__)
# And to make dataclass immutable
@dataclass(eq=True, frozen=True)
class Location:

    # Type annotations are necessary here so @dataclass can detect the class attributes
    # @dataclass will collect these class attributes and synthesise implementations of __init__, __repr__, etc.
    # Prefer immutable dataclasses and hence immutable attribute types
    name: str
    position: Position

    # Generated __init__ calls a dataclass-specific special method __post_init__
    # Useful for performing validation on data class instance construction
    def __post_init__(self):
        # Guard clause
        if self.name == "":
            raise ValueError("Location name cannot be empty")


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))

# Create instance
paris = Location("Paris", Position(38.8, 2.3))
print(repr(paris))

# Check for equality
# Note that for the synthesised __eq__ method to work, Position must also have __eq__ implemented (likewise for hash)
french_capital = Location("Paris", Position(38.8, 2.3))
print(paris == french_capital)

# Create set (hashtable-based container)
cities = {hong_kong, stockholm, cape_town, rotterdam, maracaibo}
print(cities)

# Check invariants are enforced
null_island = Location("", Position(0.0, 0.0))
