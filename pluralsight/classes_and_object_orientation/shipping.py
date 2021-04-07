class ShippingContainer:

    # Class attributes (shared between all instances of class)
    next_serial = 1337

    # Want to associate method with the class rather than the instance of the class
    # Generally prefer to use @classmethod if it requires access to the class object
    @classmethod
    def _generate_serial(cls):

        result = cls.next_serial
        cls.next_serial += 1

        return result

    '''
    # Alternatively can use static method decorator
    # Generally prefer to use @staticmethod if no access is needed to either class or instance objects
    # Most likely an implementation detail of the class
    # May be able to move 
    @staticmethod
    def _generate_serial():

        # Need to qualify reference to class attribute next_serial by prefixing with ShippingContainer
        # Since there is no class scope in Python
        # Could also use self.next_serial, but this style should be avoided
        # As distinction between instance and class attributes becomes less clear
        # Other pitfall of using self is that while we can read class attributes through the self reference
        # We cannot assign a class attribute through the self reference
        # Doing so would actually create a new instance attribute which would hide the class attribute
        result = ShippingContainer.next_serial
        # The += here does not count as an assignment
        # Since augmented assignments work as read-modify-write operations
        # This modifies the existing object (class attribute) in place
        ShippingContainer.next_serial += 1

        return result
    '''

    # Using factory function to implement method which creates an empty shipping container ("Named constructor")
    # This technique allows us to support multiple constructors with different behaviours
    @classmethod
    def create_empty(cls, owner_code):

        return cls(owner_code, contents=[])

    # Another named constructor for placing an iterable series of items in the container
    @classmethod
    def create_with_items(cls, owner_code, items):

        return cls(owner_code, contents=list(items))

    def __init__(self, owner_code, contents):

        # Instance attributes
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()


# Instance attributes
c1 = ShippingContainer("YML", ["books"])
print(c1.owner_code)
print(c1.contents)
c2 = ShippingContainer("MAE", ["clothes"])
print(c2.owner_code)
print(c2.contents)

# Getting class attribute values
c3 = ShippingContainer("ESC", ["electronics"])
print(c3.next_serial)
c3 = ShippingContainer("PEK", ["pharmaceuticals"])
print(c3.next_serial)

# Using factory function
c4 = ShippingContainer.create_empty("XYZ")
print(c4.contents)
c5 = ShippingContainer.create_with_items("CHI", {"food", "textiles", "minerals"})
print(c5.contents)
