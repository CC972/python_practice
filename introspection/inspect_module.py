import inspect
from num_vowels import num_vowels
import batch

# Check that batch is a module
print(inspect.ismodule(batch))

# Retrieve members of batch as a list of name-value pairs
# Returns everything in the module namespace, including all the built-ins
print(inspect.getmembers(batch))

# getmembers() accepts a second argument, which is a predicate function to filter the list
# The inspect module contains 16 predicates for identifying different object types
print(dir(inspect))

# Filter for classes
# As chain() is actually a class, not a function, it is also returned here alongside Batch
# It looks like a function because it violates the PEP8 naming conventions (starts with a lowercase letter)
# Calling chain() is actually invoking a constructor
# Any class defined in a module or imported into a module is in that module's namespace (hence chain is returned)
print(inspect.getmembers(batch, inspect.isclass))

# In fact, we can actually import any of these names from the batch module
# This is because import simply binds objects in another module's namespace to names in the current namespace
from batch import chain
print(list(chain([1, 2, 3], [4, 5, 6])))

# Filter for functions
print(inspect.getmembers(batch.Batch, inspect.isfunction))

# Retrieve signature object for function
init_sig = inspect.signature(batch.Batch.__init__)
print(init_sig)

# From this signature object, we can obtain a list of parameters
print(init_sig.parameters)

# We can then query individual parameters for attributes, such as their default values
print(repr(init_sig.parameters['iterables'].default))

# Can convert signature object to string
print(str(init_sig))

# Functions implemented in C (or other languages) may be missing metadata and cause signature() to fail
# inspect.signature(iter)

# We can inspect type annotations as well
sig = inspect.signature(num_vowels)
print(sig.parameters['text'])
print(sig.parameters['text'].annotation)
print(sig)
print(sig.return_annotation)

# Can also bypass inspect entirely and access the function's annotations directly
# As __annotations__ is where Python stores type annotations at runtime
print(num_vowels.__annotations__)
