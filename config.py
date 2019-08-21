import pathlib
import time
REF_TIME = time.strftime("%Y-%m-%d-%Hh%Mmin")

PROJECT_PATH: pathlib.Path = pathlib.Path(__file__).parent
DELIVERABLES_PATH: pathlib.Path = pathlib.Path(__file__).parent / 'deliverables'
DELIVERABLES_str: str = DELIVERABLES_PATH.as_posix()