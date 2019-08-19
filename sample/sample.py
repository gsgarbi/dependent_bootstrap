import random
from typing import List, Tuple, Any
import itertools

class Sample:
    def __init__(self, rolls: List[int]):
        assert all([r <= len(rolls) for r in rolls])
        self.rolls = rolls
        self.size = len(rolls)
        self.faces = list(range(1, self.size + 1))

    @classmethod
    # run __init__ with rolls = random.choices(range(1, size + 1), k=size)
    def random(cls, size=3):
        return cls(random.choices(range(1, size + 1), k=size))

    def __str__(self):
        return ''.join(('S', str(self.rolls)))

    def __repr__(self):
        return self.__str__()

    def resample(self) -> None:
        self.rolls = [Sample.pick_diff(i, self.faces) for i in self.rolls]

    @staticmethod
    def pick_diff(i: int, lis: List[int]) -> int:
        compl = [j for j in lis if j != i]
        return random.choice(compl)

    def set_values(self, values):
        assert len(values) == self.size
        self.rolls: List[int] = values
    
    @staticmethod
    def list_as_str(l) -> str:
        return ''.join(str(i) for i in l)

    def accessible_rolls(self) -> List[Tuple[Any, ...]]:
        cs = []
        for roll in self.rolls:
            compl = [j for j in self.faces if j != roll]
            cs.append(compl)
        return list(itertools.product(*cs))

    @staticmethod
    def sample_space(size):
        space = list(range(1, size + 1))
        cart_product = itertools.product(space, repeat=size)
        return [Sample(list(r)) for r in cart_product]

    def get_edges(self):
        return [(Sample.list_as_str(self.rolls), Sample.list_as_str(i)) for i in self.accessible_rolls()]

