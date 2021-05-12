import inspect
import batch

print(inspect.ismodule(batch))
print(inspect.getmembers(batch))

print(dir(inspect))
print(inspect.getmembers(batch, inspect.isclass))

from batch import chain

print(list(chain([1, 2, 3], [4, 5, 6])))
print(inspect.getmembers(batch.Batch, inspect.isfunction))

init_sig = inspect.signature(batch.Batch.__init__)
print(init_sig)
