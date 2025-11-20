from itertools import product
from random import choice

moveset = {
    "king"   : {m for m in product((-1, 0, 1), repeat=2) if m != (0,0)},
    "queen"  : ({(dx,0) for dx in range(-7,8) if dx != 0} 
             | {(0,dy) for dy in range(-7,8) if dy != 0} 
             | {(dx,dy) for n in range(1,8) for dx, dy in list(product((n, -n), repeat=2))}),
    "rook"   : ({(dx,0) for dx in range(-7,8) if dx != 0} 
             | {(0,dy) for dy in range(-7,8) if dy != 0}),
    "bishop" : {(dx,dy) for n in range(1,8) for dx, dy in list(product((n, -n), repeat=2))},
    "knight" : set(product({1,-1}, {2, -2})) | set(product({2, -2}, {1, -1})) 
}


class Simulator:
    def __init__(self, piece, square):
        self.all_moves = moveset[piece.lower()]
        self.position = (ord(square.lower()[0]) - 96, int(square[1]))

    @staticmethod
    def move(space, move):
        return space[0] + move[0], space[1] + move[1]

    def valid_moves(self):
        valid_moves = []
        for potential_move in self.all_moves:
            if (1 <= Simulator.move(self.position, potential_move)[0] <= 8 and
                1 <= Simulator.move(self.position, potential_move)[1] <= 8):
                valid_moves.append(potential_move)
        return valid_moves

    def random_walk(self, target):
        spaces = []
        while True:
            random_move = choice(self.valid_moves())
            self.position = self.move(self.position, random_move)
            spaces.append(self.position)
            if self.position == (ord(target.lower()[0]) - 96, int(target[1])):
                break
        return spaces


if __name__ == "__main__":
    tmp = Simulator("knight", "B1")
    print(tmp.random_walk("B1"))