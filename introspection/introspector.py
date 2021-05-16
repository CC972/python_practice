import inspect
import itertools
import reprlib


def dump(obj):

    print("Type")
    print("====")
    print(type(obj))
    print()

    print("Documentation")
    print("=============")
    print(inspect.getdoc(obj))  # Retrieves and tides up the docstring

    # Although getmembers() is the natural tool for getting the attributes and methods
    # We'll create our own function for pedagogical purposes
    all_attr_names = set(dir(obj))
    # Filter attributes by whether or not they are callable
    method_names = set(
        filter(lambda attr_name: callable(getattr(obj, attr_name)),
               all_attr_names)
    )
    # Assume method names are a subset of all attribute names
    assert method_names <= all_attr_names
    # Produce set of all regular (non-callable) attributes
    attr_names = all_attr_names - method_names

    print("Attributes")
    print("==========")
    # Use reprlib module to cut the values down to a reasonable size in an intelligent way
    attr_names_and_values = [(name, reprlib.repr(getattr(obj, name)))
                             for name in attr_names]
    print_table(attr_names_and_values, "Name", "Value")
    print()

    print("Methods")
    print("=======")
    methods = (getattr(obj, method_name) for method_name in method_names)
    method_names_and_doc = sorted((full_sig(method), brief_doc(method))
                                  for method in methods)
    print_table(method_names_and_doc, "Name", "Description")
    print()


def full_sig(method):

    try:
        return method.__name__ + str(inspect.signature(method))
    except ValueError:
        return method.__name__ + '(...)'


def brief_doc(obj):

    doc = obj.__doc__

    if doc is not None:
        lines = doc.splitlines()
        if len(lines) > 0:
            # Convention is that first line of docstring should be a brief description (summary)
            return lines[0]
    return ''


# Function accepts a sequence of sequences as first argument
# The outer sequence represents rows of the table, and the inner sequence represents the columns within those rows
def print_table(rows_of_columns, *headers):

    # Basic validation
    num_columns = len(rows_of_columns[0])
    num_headers = len(headers)
    if len(headers) != num_columns:
        raise TypeError("Expected {} header arguments, "
                        "got {}".format(num_columns, num_headers))

    # Lazily concatenate header and data rows into a value
    rows_of_columns_with_header = itertools.chain([headers], rows_of_columns)

    # Transpose rows of columns into columns of rows, and force evaluation of lazy zip by constructing a list
    columns_of_rows = list(zip(*rows_of_columns_with_header))

    # Find maximum width of a column
    column_widths = [max(map(len, column)) for column in columns_of_rows]

    # Need to escape outer curly braces (by doubling the curly braces) so they carry through to the result
    column_specs = ('{{:{w}}}'.format(w=width) for width in column_widths)
    format_spec = ' '.join(column_specs)
    print(format_spec.format(*headers))

    # Print horizontal rules under each header to separate them from the data
    rules = ('-' * width for width in column_widths)
    print(format_spec.format(*rules))

    # Print each row of data
    for row in rows_of_columns:
        print(format_spec.format(*row))


print(dump(7))
