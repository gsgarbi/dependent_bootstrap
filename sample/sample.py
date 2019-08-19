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
        return random.choice([j for j in lis if j != i])

    def set_values(self, values):
        assert len(values) == self.size
        self.rolls: List[int] = values
    
    @staticmethod
    def list_as_str(l) -> str:
        return ''.join(str(i) for i in l)

    def accessible_rolls(self) -> List[Tuple[Any, ...]]:
        cs = [[j for j in self.faces if j != roll] for roll in self.rolls]
        return list(itertools.product(*cs))

    @staticmethod
    def sample_space(size):
        cart_product = itertools.product(list(range(1, size + 1)),
                                         repeat=size)
        return [Sample(list(r)) for r in cart_product]

    def get_edges(self):
        return [(Sample.list_as_str(self.rolls), Sample.list_as_str(i)) for i in self.accessible_rolls()]
