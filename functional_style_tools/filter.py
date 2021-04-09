positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
print(positives)  # Lazy evaluation so only filter object is printed
print(list(positives))  # Force evaluation of results using list()

# Passing None as the first argument filters out input elements which evaluate to False in a boolean context
trues = filter(None, [0, 1, False, True, [], [1, 2, 3], '', 'hello'])
print(list(trues))  # Filters out 0, False, [], '' since they are all Falsy
