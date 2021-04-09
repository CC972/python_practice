# Comprehensions using a single input sequence
l = [i * 2 for i in range(10)]  # List
print(l)
d = {i: i * 2 for i in range(10)}  # Dictionary
print(d)
s = {i for i in range(10)}  # Set
print(s)
g = (i for i in range(10))  # Generator
print(g)

# Multiple input sequences
print([(x, y) for x in range(5) for y in range(5)])  # Equivalent to nested for-loops

# Can use multiple for/if clauses
values = [x / (x - y)
          for x in range(100)
          if x > 50
          for y in range(100)
          if x - y != 0]

# Later clauses can refer to variables bound in earlier clauses
print([(x, y) for x in range(10) for y in range(x)])

# Set comprehension
print({x * y for x in range(10) for y in range(10)})

# Generator comprehension
print(((x, y) for x in range(10) for y in range(10)))
# Lazy so need to force evaluation
print(list(((x, y) for x in range(10) for y in range(x))))
