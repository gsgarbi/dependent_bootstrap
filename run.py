import logging
import sys
from pathlib import Path
from chain import Chain, plot
from sample import Sample

# create folders
from utils.path_tools import plot_chain

PROJECT_FOLDER = Path(__file__).parent
TARGET_FOLDER = 'deliverables'
fn = PROJECT_FOLDER.joinpath(TARGET_FOLDER)
fn.mkdir(exist_ok=True)

logger = logging.getLogger(__file__)
logger.setLevel(logging.CRITICAL)


def simulate():
    # read size
    try:
        size = int(sys.argv[1])
        if size <= 2:
            logger.critical("size needs to be > 2")
        initial_sample = Sample.random(size)
    except IndexError:
        initial_sample = Sample.random()
        logger.warning("No size given. Using size = {}".format(initial_sample.size))

    chain = Chain(initial_sample)
    chain.create_path()
    logger.debug('chain type {}\nSimulated Chain: {}'.format(
        chain, type(chain.samples[0].rolls)))
    chain.save()
    logger.info(chain)
    plot.chain()
