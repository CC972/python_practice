def hypervolume(length, *lengths):

    v = length
    for length in lengths:
        v *= length
    return v


# Length of line
print(hypervolume(1))

# Area of rectangle
print(hypervolume(2, 4))

# Volume of cuboid
print(hypervolume(2, 4, 6))

# Hypervolume of hypercuboid
print(hypervolume(2, 4, 6, 8))