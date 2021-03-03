def wrap(text, line_length):
    """Function which wraps strings of text at a specified line length"""

    # Raise exception to handle bad data from the caller
    # Do not use assertions as validation guards
    if line_length < 1:
        raise ValueError("line_length {} is not positive".format(line_length))

    words = text.split()

    # Reject words longer than the line length
    if (max(map(len, words))) > line_length:
        raise ValueError("line_length must be at least as long as the longest word")

    lines_of_words = []
    current_line_length = line_length

    for word in words:
        if current_line_length + len(word) > line_length:
            lines_of_words.append([])  # New line
            current_line_length = 0
        lines_of_words[-1].append(word)
        # Fix as a result of the assertion
        current_line_length += len(word) + len(' ')  # Calculate length of space explicitly to avoid magic numbers

    lines = [' '.join(line_of_words) for line_of_words in lines_of_words]

    result = '\n'.join(lines)

    # Check length of each line does not exceed desired line length
    # Assertion reveals that we need to account for length of the additional space when rejoining the words
    assert all(len(line) <= line_length for line in result.splitlines()), "Line too long"

    return result


assertions_doc = "A few techniques can help shift the numbers in our favor, including good error logging, good " \
    "testing, and internal self-checks (assertions). I wanted to write briefly about how assertions can help with " \
    "Python code. Assertions are a systematic way to check that the internal state of a program is as the " \
    "programmer expected, with the goal of catching bugs. In particular, they're good for catching false " \
    "assumptions that were made while writing the code, or abuse of an interface by another programmer. In " \
    "addition, they can act as in-line documentation to some extent, by making the programmer's assumptions obvious."

print(wrap(assertions_doc, 25))

# Passing in a negative line length would be the caller's mistake, so such cases should not be handled using assertions
# Users will interpret assertion failures as errors in the implementation
print(wrap(assertions_doc, -25))

# Case where text contains a word longer than line length
print(wrap('The next train to Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch is at 16:32', 25))
