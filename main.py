from random import choice

from knight import Knight

def main():
    knight = Knight()
    moves = 0
    while True:
        print(knight.space)
        random_move = choice(knight.valid_moves())
        knight.move_piece(random_move)
        moves += 1

        if knight.space == (2,1):
            print(knight.space)
            print(f"No of moves: {moves}")
            break


if __name__ == "__main__":
    main()