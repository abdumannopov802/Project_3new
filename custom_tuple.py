class IterableObject():
    def __init__(self, sequence) -> None:
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

a = IterableObject("salom")
for i in a:
    print(i)

b = list(a)
print(type(a))


# NamedTuple
from collections import namedtuple

newTuple = namedtuple('My_tuple', 'x y z')
b = newTuple(1, 2, 3)
print(type(b), b)
b = set(b)
print(type(b))