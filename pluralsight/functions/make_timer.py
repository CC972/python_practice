import time


def make_timer():
    """Returns elapsed function"""

    last_called = None

    def elapsed():
        """Returns elapsed time since last called"""

        nonlocal last_called  # Used as form of persistent storage

        now = time.time()

        if last_called is None:
            last_called = now
            return None

        result = now - last_called
        last_called = now
        return result

    return elapsed


t = make_timer()
print(t())
time.sleep(1)
print(t())
time.sleep(2)
print(t())
