import matplotlib.pyplot as plt
import numpy as np

from src.data.load.load_training_datasets import bitstamp_1_min_transaction, nasqad_historical
from src.processing.join import change_date_to_column


def main_historical_graph():
    """
    A function that creates a graph of the historical data.
    Saves the graph to a file.
    """
    bit_csv = bitstamp_1_min_transaction(
        "src/data/bitstamp-1-min-transaction-2012-2017.csv",
    )

    change_date_to_column(bit_csv, is_timestap=True)

    # grid the plots
    plt.figure(num=None, figsize=(20, 6))
    plt.subplot(1, 2, 1)

    ax = bit_csv['Close'].plot(style=['-'])
    ax.lines[0].set_alpha(0.3)
    ax.set_ylim(0, np.max(bit_csv['Close'] + 100))
    plt.xticks(rotation=90)
    plt.title("No scaling")
    ax.legend()
    plt.subplot(1, 2, 2)
    ax = bit_csv['Close'].plot(style=['-'])
    ax.lines[0].set_alpha(0.3)
    ax.set_yscale('log')
    ax.set_ylim(0, np.max(bit_csv['Close'] + 100))
    plt.xticks(rotation=90)
    plt.title("logarithmic scale")
    ax.legend()

    # save the figure to file
    plt.savefig('src/graphs/images/historical-graph.png')


def load():
    print(nasqad_historical())


if __name__ == "__main__":
    load()
