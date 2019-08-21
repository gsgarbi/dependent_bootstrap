import csv
from config import DELIVERABLES_PATH
import pathlib as pl
from typing import List

def save_here(data: List[list], rel_path: str):
    """
    """
    file_path: pl.Path = DELIVERABLES_PATH / rel_path
    parent: pl.Path = file_path.parent
    if not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)

    with file_path.open('w') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# if __name__ == '__main__':
#     name = 'save3/here/sddwklksdflswq/{}'.format(REF_TIME)
#     save_here([[1, 2], [2, 3]], name)