import iso6346


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

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
        )

    # Using factory function to implement method which creates an empty shipping container ("Named constructor")
    # This technique allows us to support multiple constructors with different behaviours
    # Use extended argument syntax as factory methods will not know about the signature of __init__ in subclasses
    # In general, good OOP design requires that base classes have no knowledge of subclasses
    @classmethod
    def create_empty(cls, owner_code, **kwargs):

        return cls(owner_code, contents=[], **kwargs)

    # Another named constructor for placing an iterable series of items in the container
    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):

        return cls(owner_code, contents=list(items), **kwargs)

    def __init__(self, owner_code, contents, **kwargs):

        # Instance attributes
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(  # Use polymorphic dispatch static method through the instance, self
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


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

# Checking BIC code
c6 = ShippingContainer.create_empty("ELF")
print(c6.bic)


# Subclass of ShippingContainer (base class)
class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    # Override initializer from base class
    # Use * to make celsius a keyword-only argument
    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        # In other OOP languages, constructors at every level in an inheritance hierarchy are called automatically
        # But in Python we need to explicitly call the base class initializer when overriding it in a derived class
        super().__init__(owner_code, contents, **kwargs)
        # Use self encapsulation to re-use the temperature validation logic
        # Even attributes internal to the class go through the property getter and setter
        # Rather than directly accessing the underlying attribute
        # Useful technique for helping maintaining class invariants (e.g. temperature constraint)
        self.celsius = celsius

    # Following methods to perform temperature conversions are good candidates for static methods
    # Since they don't depend on instance or class objects, but don't belong in the global scope either
    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        return (fahrenheit - 32) * 5/9

    # Getters and setters are not pythonic
    # Instead we encapsulate getter and setter methods in properties which behave like attributes
    # Read-only attribute (getter)
    @property
    def celsius(self):
        return self._celsius

    # Setter method
    @celsius.setter
    def celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        self._celsius = value

    # Properties don't have to be backed by attributes and can be computed on the fly
    @property
    def fahrenheit(self):
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    # Static method with inheritance
    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category="R"  # Only difference is that we are passing R as category
        )


# Check BIC code
r1 = RefrigeratedShippingContainer("RCO", ["fish"], celsius=1.0)
print(r1.bic)

# Class methods are also inherited
# Object gets created with the appropriate subtype
# Behaviour of class methods behaving polymorphically is a distinguishing feature of Python
# These invocations work because the base class __init__ method is inherited into the subclass
r2 = RefrigeratedShippingContainer.create_empty("XML", celsius=3.0)
print(r2)
r3 = RefrigeratedShippingContainer.create_with_items("GUO", ["ice", "peas"], celsius=0.0)
print(r3)

# Construct instance derived class using factory function in base class
r4 = RefrigeratedShippingContainer.create_with_items("ESC", ["onions"], celsius=2.0)
print(r4)
print(r4.bic)
print(r4.contents)
print(r4.celsius)

# Can access attribute value celsius using the regular attribute access syntax (as opposed to function call)
# The property decorator converts the celsius method such that when accessed, it behaves like an attribute
r5 = RefrigeratedShippingContainer.create_with_items("YOU", ["yoghurt"], celsius=-18.0)
print(r5.celsius)

# Set temperature
# Attempting to set the temperature above MAX_CELSIUS raises an error, so class invariant is maintained
r6 = RefrigeratedShippingContainer.create_with_items("DEE", ["prawns"], celsius=-18.0)
r6.celsius = -19.0
print(r6.celsius)

# Get and set temperature in fahrenheit
r7 = RefrigeratedShippingContainer.create_empty("LMN", celsius=-20.0)
print(r7.fahrenheit)
print(r7.celsius)
r7.fahrenheit = -5.0
print(r7.fahrenheit)
print(r7.celsius)
