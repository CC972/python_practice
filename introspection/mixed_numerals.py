from fractions import Fraction


def mixed_numeral(vulgar):

    try:
        integer = vulgar.numerator // vulgar.denominator
        fraction = Fraction(vulgar.numerator - integer * vulgar.denominator,
                            vulgar.denominator)

        return integer, fraction
    except AttributeError as e:
        raise TypeError("{} is not a rational number".format(vulgar)) from e  # Explicit exception chaining


# Case where input can be converted to a mixed fraction
print(mixed_numeral(Fraction('11/10')))

# Case where input cannot be converted to a mixed fraction (raises error)
print(mixed_numeral(1.7))
