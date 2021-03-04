"""Rewriting LoggingContextManager using the contextmanager decorator"""

import contextlib
import sys


# Use contextmanager decorator to create context manager from generator
# Benefit of using a generator is that it avoids the need to break context manager logic across two methods
# And since generators remember their state, they can be used to implement statement context managers
@contextlib.contextmanager
def logging_context_manager():

    # Everything before yield part is conceptually part of __enter__()
    print('logging_context_manager: enter')

    try:
        yield "You're in a with-block!"
        # Everything after yield is conceptually part of __exit__()
        print("logging_context_manager: normal exit")
    except Exception:
        print('logging_context_manager: exceptional exit',
              sys.exc_info())
        # Exceptions are dealt with using normal exception handling tools for context managers created via decorators
        # So need to re-raise to propagate exception out of with-block
        raise


# Normal exit
with logging_context_manager() as x:
    print(x)


# Exceptional exit
with logging_context_manager() as x:
    raise ValueError('Something went wrong!')
