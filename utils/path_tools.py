import csv
from config import DELIVERABLES_PATH
import pathlib as pl
from typing import List
from matplotlib import pyplot as plt

def setup(file_path):
    parent = file_path.parent
    if not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)

def save_chain(data: List[list], rel_path: str):
    """
    """
    file_path: pl.Path = DELIVERABLES_PATH / rel_path
    setup(file_path)
    with file_path.open('w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def read_data(rel_path) -> List[list]:
    file_path: pl.Path = DELIVERABLES_PATH / rel_path
    with file_path.open('r') as f:
        reader = csv.reader(rel_path)
        data = reader
    return data

def plot_chain(samples: List[list]):
    pass



# if __name__ == '__main__':
#     name = 'save3/here/sddwklksdflswq/{}'.format(REF_TIME)
#     save_chain([[1, 2], [2, 3]], name)