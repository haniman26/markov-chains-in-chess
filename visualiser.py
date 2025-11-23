import matplotlib.pyplot as plt
import numpy as np

type Space = tuple[int,int]
type Move = tuple[int,int]

"""Code to visualise the frequency table for one particular random walk"""
def frequency_graph(spaces_visited: list[Space], filename: str = "Frequency Table.png"):
    frequency_table = np.zeros((8,8))
    for space in spaces_visited:
        frequency_table[8-space[1]][space[0]-1] += 1
    plt.imshow(frequency_table, cmap="Reds")
    plt.xticks(range(8), list('ABCDEFGH'))
    plt.yticks(range(8), range(8, 0, -1))
    plt.tick_params(axis='both', which='both', length=0)
    # Move gridlines to between cells instead of on cells
    plt.gca().set_xticks([x - 0.5 for x in range(1, 8)], minor=True)
    plt.gca().set_yticks([y - 0.5 for y in range(1, 8)], minor=True)
    plt.grid(which='minor', color='black', linewidth=1)
    plt.colorbar()
    plt.show()
    return frequency_table

if __name__ == "__main__":
    print(frequency_graph([(2,1),(3,3),(2,1)]))