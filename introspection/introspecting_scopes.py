# Returns a dictionary representing (or rather, is) the global namespace
print(globals())

# Can see that binding of name to value 42 is added to the global namespace
a = 42
print(globals())

# Can assign new key-value pairs
globals()['tau'] = 6.283185
print(tau)

# Returns dictionary representing local scope
print(locals())


# Create another scope to demonstrate local scope
def report_scope(arg):

    from pprint import pprint as pp

    x = 496
    pp(locals(), width=10)


report_scope(42)

# Extended syntax allows us to unpack a dictionary into a function's keyword arguments
# str.format() accepts keyword arguments that correspond to format placeholders
# Combining the two, we can refer to local variables in format strings
name = "Joe Bloggs"
age = 28
country = "New Zealand"
print("{name} is {age} years old and is from {country}".format(**locals()))

# Better practice is to use f-strings when possible
print(f"{name} is {age} years old and is from {country}")
