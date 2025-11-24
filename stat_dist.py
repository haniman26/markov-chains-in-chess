from random import choice
import numpy as np

from random_walk import *
from visualiser import frequency_graph

def main():
    simulation = Simulator("knight", "b1")
    spaces_visited = simulation.random_walk(n=1000000)
    stat_dist = frequency_graph(spaces_visited) / (1000000 + 1)
    print(stat_dist)
    print(np.sum(stat_dist))
    print("\nCalculated stat dist")
    calc_stat_dist = np.array([[2,3,4,4,4,4,3,2],
                               [3,4,6,6,6,6,4,3],
                               [4,6,8,8,8,8,6,4],
                               [4,6,8,8,8,8,6,4],
                               [4,6,8,8,8,8,6,4],
                               [4,6,8,8,8,8,6,4],
                               [3,4,6,6,6,6,4,3],
                               [2,3,4,4,4,4,3,2]]) / 336
    print(calc_stat_dist)
    print(np.sum(calc_stat_dist))
    print("\nAvg Error btwn calc and sim")
    print(np.mean(np.absolute(stat_dist - calc_stat_dist)))


if __name__ == "__main__":
    main()