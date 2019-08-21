import logging

from config import REF_TIME
from sample.sample import Sample
from utils.path_tools import save_chain

logger = logging.getLogger(__file__)
logger.setLevel(logging.WARNING)


class Chain:

    def __init__(self, initial_sample: Sample):
        self.samples = [initial_sample]

    def create_path(self, length=100):
        for _ in range(length):
            self.move()

    def move(self):
        last_sample = Sample(self.samples[-1].rolls)
        last_sample.resample()
        self.samples.append(last_sample)

    def save(self):
        rolls = [s.rolls for s in self.samples]
        save_chain(rolls, REF_TIME)

    def plot(self):
        pass

    def __str__(self):
        result = str(self.samples[0])
        for s in self.samples[1:]:
            result += " -> {}".format(s)
        return result

    def __repr__(self):
        return self.__str__()
