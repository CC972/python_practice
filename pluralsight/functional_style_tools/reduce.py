from functools import reduce
import operator

print(reduce(operator.add, [1, 2, 3, 4, 5]))


# Demonstration of how reduce works
numbers = [1, 2, 3, 4, 5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
    accumulator = operator.add(accumulator, item)
print(accumulator)


def mul(x, y):
    print('{} × {}'.format(x, y))  # Print operations to show how reduce works
    return x * y


result = reduce(mul, range(1, 10))
print(result)

# Can specify an optional initial value, which conceptually is just added to the beginning of the sequence
# This serves as the first accumulator value
# Useful to have when you are not sure if your input will have any values
# Since passing an empty sequence to reduce raises a TypeError
values = [1, 2, 3]
print(reduce(operator.add, values, 0))  # Use 0 as initial value for summation
print(reduce(operator.mul, values, 1))  # Use 1 as initial value for products
