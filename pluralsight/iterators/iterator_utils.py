"""Useful methods for iterators"""


def _is_perfect_length(sequence):
    """True if sequence has length 2ⁿ - 1, otherwise False
    """
    n = len(sequence)

    # Don't allow empty trees
    return ((n + 1) & n == 0) and (n != 0)


def _left_child(index):
    """Helper function to return index of left child
    given index of parent"""
    return 2 * index + 1


def _right_child(index):
    """Helper function to return index of right child
    given index of parent"""
    return 2 * index + 2