def game_board():
    rows, cols = (5, 5)
    board = [[0] * cols] * rows
    for row in board:
        print(row)


def main():
    game_board()


if __name__ == "__main__":
    main()
