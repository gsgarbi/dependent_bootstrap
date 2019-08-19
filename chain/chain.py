from sample.sample import Sample
from pathlib import Path
import csv
import logging
import datetime as dt

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

        txt = """Next sample is obtained by changing the"
        "values of all rolls"""
        samples = self.samples
        TARGET_FOLDER = 'deliverables'
        FILE_NAME = 'mc_simulation_{}.csv'.format(dt.datetime.today())
        PROJECT_FOLDER = Path(__file__).parent.parent
        fn = PROJECT_FOLDER.joinpath(TARGET_FOLDER)
        # TODO make create parent dirs
        fn.mkdir(exist_ok=True)
        path: str = '/'.join([fn.as_posix(), FILE_NAME])
        number_faces = Sample(self.samples[-1].rolls)

        spl_rolls = [s.rolls for s in samples]

        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(spl_rolls)

    def __str__(self):
        result = str(self.samples[0])
        for s in self.samples[1:]:
            result += " -> {}".format(s)
        return result

    def __repr__(self):
        return self.__str__()