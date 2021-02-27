"""Implementation of run length encoding"""


def compress(text):

    buffer = []

    prev_char = None
    prev_ctr = 0

    for char in text:
        if char != prev_char:
            if prev_char is not None:
                buffer += f"{chr(prev_ctr)}{prev_char}"
            prev_char = char
            prev_ctr = 0
        prev_ctr += 1

    if prev_char is not None:
        buffer += f"{chr(prev_ctr)}{prev_char}"

    return ''.join(buffer)


def decompress(text):

    buffer = []
    prev_char = None
    for idx, char in enumerate(text):
        if idx % 2:
            buffer += char * ord(prev_char)
        prev_char = char

    return ''.join(buffer)


assert 100 * 'k' == decompress('dk')
