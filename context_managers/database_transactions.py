"""Demonstrating robust resource handling with context managers by modelling database transactions"""

import contextlib


class Connection:

    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print('Starting transaction', self.xid)
        result = self.xid
        self.xid = self.xid + 1  # Increment transaction ID when new transaction is started
        return result

    def _commit_transaction(self, xid):
        print('Commiting transaction', xid)

    def _rollback_transaction(self, xid):
        print('Rolling back transaction', xid)


class Transaction:

    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self):
        self.conn._rollback_transaction(self.xid)


# Place logic for properly handling transactions into a context manager
@contextlib.contextmanager
def start_transaction(connection):

    tx = Transaction(connection)

    try:
        yield
    except:
        # Exceptional exit
        tx.rollback()
        raise

    # Normal exit
    tx.commit()


conn = Connection()


# Exceptional case
try:
    # Use context manager so commit/rollback is handled automatically
    with start_transaction(conn):
        x = 1 + 1
        raise ValueError()  # Intentionally raise ValueError to demonstrate rollback
        y = x + 2
        print(f'transaction => {x} {y}')
except ValueError:
    print('Operation failed')

# Normal case
try:
    with start_transaction(conn) as tx:
        x = 1 + 1
        y = x + 2
        print(f'transaction => {x} {y}')
except ValueError:
    assert False
