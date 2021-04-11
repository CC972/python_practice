import functools
import inspect

from location import hong_kong, stockholm, cape_town, rotterdam, maracaibo, auto_repr


# Function decorator factory
# Predicate function returns true or false
def postcondition(predicate):

    def function_decorator(f):

        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            result = f(self, *args, **kwargs)
            if not predicate(self):
                raise RuntimeError(
                    f"Post-condition {predicate.__name__} not "
                    f"maintained for {self!r}"
                )
            return result

        return wrapper

    return function_decorator


# Use class decorator factory
# Because using function decorator would mean decorating several of the class methods manually
# Want to be able to parametrise decorator with postcondition predicate
def invariant(predicate):

    function_decorator = postcondition(predicate)

    def class_decorator(cls):

        members = list(vars(cls).items())  # Take copy

        for name, member in members:
            if inspect.isfunction(member):
                # If the member is a function, decorate it with the function decorator
                decorated_member = function_decorator(member)
                setattr(cls, name, decorated_member)

        return cls

    return class_decorator


def at_least_two_locations(itinerary):
    return len(itinerary._locations) >= 2


def no_duplicates(itinerary):

    already_seen = set()

    for location in itinerary._locations:
        if location in already_seen:
            return False
        already_seen.add(location)
    return True


@auto_repr
@invariant(no_duplicates)
@invariant(at_least_two_locations)
class Itinerary:

    # Factory pattern, named constructor and a convenience function
    # Forwards locations to main constructor
    @classmethod
    def from_locations(cls, *locations):
        return cls(locations)

    def __init__(self, locations):
        self._locations = list(locations)

    def __str__(self):
        return "\n".join(location.name for location in self._locations)

    @property
    def locations(self):
        return tuple(self._locations)

    @property
    def origin(self):
        return self._locations[0]

    @property
    def destination(self):
        return self._locations[-1]

    def add(self, location):
        self._locations.append(location)

    def remove(self, name):
        removal_indexes = [
            index for index, location in enumerate(self._locations)
            if location.name == name
        ]
        for index in reversed(removal_indexes):
            del self._locations[index]

    def truncate_at(self, name):
        stop = None
        for index, location in enumerate(self._locations):
            if location.name == name:
                stop = index + 1

        self._locations = self._locations[:stop]


trip = Itinerary.from_locations(maracaibo, rotterdam, stockholm)
print(trip)
print(trip.locations)
print(trip.origin)
print(trip.destination)
trip.add(cape_town)
trip.add(hong_kong)
trip.remove("Stockholm")
print(trip.locations)
trip.truncate_at("Rotterdam")
print(trip.locations)

# Testing out class decorator
# Raises error as class invariant prevents us from creating an itinerary with just one location
trip_1 = Itinerary.from_locations(rotterdam)  # Fails at least two locations check
trip_2 = Itinerary.from_locations(rotterdam, stockholm)  # Succeeds
trip_2.remove("Stockholm")  # Fails at least two locations check
trip_3 = Itinerary.from_locations(rotterdam, rotterdam)  # Fails no duplicate check
