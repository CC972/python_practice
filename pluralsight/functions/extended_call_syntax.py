def print_args(arg1, arg2, *args):
    print("arg1 = ", arg1)
    print("arg2 = ", arg2)
    print("args = ", args)


# Using a tuple to populate positional arguments
t = (11, 12, 13, 14)
print_args(*t)


def colour(red, green, blue, **kwargs):
    print("r = ", red)
    print("g = ", green)
    print("b = ", blue)
    print("kwargs = ", kwargs)


# Using a dictionary to populate keyword arguments
k = {'red': 21, 'green': 68, 'blue': 120, 'alpha': 52}
colour(**k)


