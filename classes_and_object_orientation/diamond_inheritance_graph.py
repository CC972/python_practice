class A:
    def func(self):
        return 'A.func'


class B(A):
    def func(self):
        return 'B.func'


class C(A):
    def func(self):
        return 'C.func'


class D(B, C):
    pass


# Python checks D first, followed by B, C, A, then finally object (ultimate base class for all classes in Python)
print(D.__mro__)

# Resolves to B's func() because B is the first class Python finds which defines the func() method
d = D()
print(d.func())
