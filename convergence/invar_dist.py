import sys
from typing import List, Union

import numpy as np

from sample.sample import Sample


def isdist(d: list) -> bool:
    """
    check if d is a valid distribution
    :param d: ndarray
    """
    return np.isclose(sum(d), 1) and all(d) >= 0


def build_P() -> None:
    """
    build transtion matrix
    :return:
    """
    for s in SPACE:
        acc_states = s.acc_states()  # avoid computing many times
        line = [(t in acc_states) / len(acc_states) for t in SPACE]
        P.append(line)
    pass


def isinvariant(K: Union[List[List], np.ndarray], d: Union[list, np.ndarray]) -> bool:
    """
    returns True if d * K == d
    :param K: kernel
    :param d: distribution
    :return: bool
    """
    return np.allclose(np.dot(K, d), d)


if __name__ == '__main__':
    try:
        FACES = int(sys.argv[1])
    except IndexError:
        FACES = 3
    SPACE: List[Sample] = Sample.sample_space(FACES)

    P: List[List[float]] = list()
    build_P()
    unif_dist = np.ones(shape=len(SPACE)) / len(SPACE)
    assert isdist(unif_dist)

    if isinvariant(P, unif_dist):
        print(f'the uniform distribution is invariant for FACES={FACES}')
