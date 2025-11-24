import numpy as np

from random_walk import *
from visualiser import recurrence_times

def main():
    simulation = Simulator("knight", "b1")
    random_walks = []
    for _ in range(10000):
        random_walks.append(simulation.random_walk(target="b1"))
    lengths = recurrence_times(random_walks)
    print(np.mean(lengths))

if __name__ == "__main__":
    main()