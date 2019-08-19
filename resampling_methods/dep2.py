import random
from typing import List

def resample(l):
    """
    # does not work since [1,2,3] is not accessible by any sample/state
    :param l:
    :return:
    """
    all_ = range(1, len(l) + 1)
    not_present = list(set(all_).difference(set(l)))

    if not not_present:
        new = random.choices(l, k=len(li))
    else:
        new = random.choices(not_present, k=len(l))

    return new

if __name__ == '__main__':
    li = [3, 3, 3, 3, 3]
    print(resample(li))