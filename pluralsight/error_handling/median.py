def median(iterable):

    items = sorted(iterable)
    median_index = (len(items) - 1) // 2

    # Guard clause to check series is non-empty
    if len(items) == 0:
        raise ValueError("median() arg is an empty series")

    if len(items) % 2 != 0:
        return items[median_index]

    return (items[median_index] + items[median_index + 1]) / 2


# To programmatically retrieve the error message
def main():
    try:
        median([])
    except ValueError as e:
        # Ways to retrieve the exception payload
        print("Payload:", e.args)
        print("Payload repr:", repr(e))  # repr version shows exception type
        print("Payload str:", str(e))  # while str version simply shows payload


main()

