import random
from typing import List

def pick_diff(i: int, lis: List[int]) -> int:
    compl = [j for j in lis if j != i]
    return random.choice(compl)

def resample(li: List[int]):
    # for each roll
    # pick a different value randomly

    space = list(range(1, len(li) + 1))
    for k in range(len(li)):
        li[k] = pick_diff(k, space)




