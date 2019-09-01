import math
from typing import List

import numpy as np

from sample import Sample

# dice number of faces, e.g, 3
NUM_FACES = 3
SAMPLE_SPACE = Sample.sample_space(NUM_FACES)

# build transition matrix P
P: List[List[float]] = list()
s: Sample
t: Sample
for s in SAMPLE_SPACE:
    # entries of <line> are the probabilties of s going to t:
    line: List[float] = list()
    for t in SAMPLE_SPACE:
        # as defined by our chosen s.resample()
        # method in sample.Sample:
        if t in s.accessible_states():
            prob_s_t = 1 / len(s.accessible_states())
        else:
            prob_s_t = 0
        line.append(prob_s_t)
    assert np.isclose(sum(line), 1)

    P.append(line)

# dist as defined below will be the invariant distribution
dist = np.ones(shape=len(SAMPLE_SPACE)) / len(SAMPLE_SPACE)
assert math.isclose(sum(dist), 1)
assert np.allclose(np.dot(P, dist), dist)
