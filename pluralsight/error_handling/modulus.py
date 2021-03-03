def modulus_three(n):

    r = n % 3

    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Remainder 1")
    else:
        assert r == 2, "Remainder is not 2"
        print("Remainder 2")


# If we want to copy the above function but adapt it to calculate modulus four
# We cannot simply change the places where there are 3 to 4
# For some inputs, the assertion would be violated
# Which helps us to identify the problem and correct the problem


def modulus_four(n):

    r = n % 4

    if r == 0:
        print("Multiple of 4")
    elif r == 1:
        print("Remainder 1")
    elif r == 2:
        print("Remainder 2")
    else:
        assert r == 3, "Remainder is not 3"
        print("Remainder 3")


# We can make the assertion even more explicit by placing it in a separate else block


def modulus_four(n):

    r = n % 4

    if r == 0:
        print("Multiple of 4")
    elif r == 1:
        print("Remainder 1")
    elif r == 2:
        print("Remainder 2")
    elif r == 3:
        print("Remainder 3")
    else:
        assert False, "This should never happen"
