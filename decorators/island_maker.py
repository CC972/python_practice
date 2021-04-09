"""Using decorators on class methods"""


from trace import Trace


tracer = Trace()


class IslandMaker:

    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix


im = IslandMaker(' Island')
print(im.make_island('Python'))
