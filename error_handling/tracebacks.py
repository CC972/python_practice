from traceback import print_tb
from explicit_chaining import inclination, InclinationError


def main():

    try:
        inclination(0, 5)
    except InclinationError as e:
        print(e.__traceback__)
        print_tb(e.__traceback__)

    print("Finished")


main()
