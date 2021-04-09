import socket
from timeit import timeit


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache


# Implementing the __call__ allows us to call the class like a function
resolve = Resolver()

print(resolve('sixty-north.com'))
print(resolve._cache)
print(resolve('pluralsight.com'))
print(resolve._cache)

# Performance testing
# Need to import from REPL namepsace into the timeit namespace
print("DNS lookup time without caching: ", timeit(setup="from __main__ import resolve", stmt="resolve('google.com')", number=1))
print("DNS lookup time with caching: ", timeit(setup="from __main__ import resolve", stmt="resolve('google.com')", number=1))

print(resolve.has_host("pluralsight.com"))
print(resolve.has_host("reddit.com"))
resolve.clear()
resolve.has_host("pluralsight.com")
