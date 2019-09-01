from __future__ import annotations
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

    def __eq__(self, other: Sample):
        return self.rolls == other.rolls

    def resample(self) -> None:
        """
        randomly change each roll to a different roll
        :return: None
        """
        self.rolls = [Sample.pick_diff(i, self.faces)
                      for i in self.rolls]

    @staticmethod
    def pick_diff(i: int, lis: List[int]) -> int:
        return random.choice([j for j in lis if j != i])

    def set_values(self, values):
        assert len(values) == self.size
        self.rolls: List[int] = values

    @staticmethod
    def list_as_str(l) -> str:
        return ''.join(str(i) for i in l)

    def accessible_states(self) -> List[Sample]:
        acc_r = []

        for s in Sample.sample_space(self.size):
            i = 0
            for i in range(self.size):
                if s.rolls[i] == self.rolls[i]:
                    break
            else:
                acc_r.append(s)

        return acc_r

    @staticmethod
    def sample_space(size) -> List[Sample]:
        cart_product = itertools.product(list(range(1, size + 1)),
                                         repeat=size)
        return [Sample(list(r)) for r in cart_product]

    def get_edges(self):
        return [(Sample.list_as_str(self.rolls),
                 Sample.list_as_str(i)) for i in self.accessible_states()]
