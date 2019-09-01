# credits to https://stackoverflow.com/users/1222578/marius for basic code
import sys
from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt
import logging
from sample.sample import Sample as S
logging.basicConfig(level=logging.WARNING)

def chain():
    if not sys.warnoptions:
        import warnings
        warnings.simplefilter("ignore")

    # create graph
    # moves are reversible, so we don't need a Directional Graph(DiGraph())
    G = nx.Graph()

    # if want to plot all:
    # use S.SAMPLE_SPACE(sample_space_size)
    sample_example = S([1, 2, 3])
    DESIRED_SAMPLES = S([1, 2, 3]), S([2, 1, 2]), S([3, 3, 3]), S([1, 1, 1])
    # add edges to graph
    [G.add_edges_from(s.get_edges()) for s in DESIRED_SAMPLES]

    # Need to create a layout when doing separate calls to draw nodes and edges
    pos = nx.spring_layout(G, seed=11)
    nx.draw_networkx_nodes(G, pos, node_color='orange', node_size=700)
    nx.draw_networkx_labels(G, pos, font_color='blue', font_weight='normal')
    nx.draw_networkx_edges(G, pos, arrows=False, alpha=0.3)

    title_ = ', '.join(S.list_as_str(s.rolls) for s in DESIRED_SAMPLES)
    plt.title("4 samples in MC when die has {} faces: {}\n"
              "Move def: change all rolls".format(sample_example.size, title_))

    TARGET_FOLDER = 'deliverables'
    FILE_NAME = 'mc_plot'
    PROJECT_FOLDER = Path(__file__).parent.parent
    fn = PROJECT_FOLDER.joinpath(TARGET_FOLDER)
    fn.mkdir(exist_ok=True)
    path: str = '/'.join([fn.as_posix(), FILE_NAME])


    plt.savefig(fname=path)
