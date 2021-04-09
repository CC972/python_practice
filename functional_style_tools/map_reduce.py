from functools import reduce


def count_words(doc):
    """Returns the number of occurrences of each word in a document in the form of a dictionary"""

    normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}

    for word in normalised_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1  # Return value of 0 if key not found

    return frequencies


print(count_words('It was the best of times, it was the worst of times.'))

documents = [
    'MapReduce framework (or system) is usually composed of three operations (or steps)',
    'Map: each worker node applies the map function to the local data, and writes the output to a temporary storage',
    'A master node ensures that only one copy of the redundant input data is processed',
    'Shuffle: worker nodes redistribute data based on the output keys (produced by the map function)',
    'Such that all data belonging to one key is located on the same worker node',
    'Reduce: worker nodes now process each group of output data, per key, in parallel',
]

counts = map(count_words, documents)


def combine_counts(d1, d2):
    """Takes two word-count dictionaries and combines them"""

    d = d1.copy()  # Shallow copy

    for word, count in d2.items():
        d[word] = d.get(word, 0) + count

    return d


# Produce a dictionary containing the word counts over all the documents in the list
total_counts = reduce(combine_counts, counts)
print(total_counts)
