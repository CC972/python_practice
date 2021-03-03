class LoggingContextManager:

    def __enter__(self):

        print('LoggingContextManager.__enter__()')
        return "You're in a with-block!"

    def __exit__(self, exc_type, exc_val, exc_tb):

        # Can control the propagation of an exception through return value
        # Return False to propagate exception and True to swallow it

        if exc_type is None:
            print('LoggingContextManager.__exit__: '
                  'Normal exit detected')
        else:
            # These arguments are None if the block exits normally
            # Otherwise they'll contain information about the exception
            print('LoggingContextManager.__exit__: '
                  'Exception detected! '
                  'type={}, value={}, traceback={}'.format(exc_type, exc_val, exc_tb))


with LoggingContextManager() as x:
    print(x)

with LoggingContextManager() as x:
    raise ValueError("Something has gone wrong!")
